import csv
import os
from comboio import Comboio
from fila import Fila
from passageiro import Passageiro
from viagem import Viagem
from bilheteira import Bilheteira
from pilha import Pilha
from tempo import str_to_minutos, minutos_to_str

class Estacao:
    def __init__(self, params):
        self.params = params
        self.parque = Pilha()
        self.viagens = []
        self.passageiros = []
        self.placar = []
        self.seguidores = {}
        self.questoes_seguidores = []
        self.erros = []

    def carregar_parque(self, path):
        with open(path) as f:
            for linha in f:
                self.parque.push(Comboio(linha.strip()))

    def carregar_passageiros(self, path):
        abertura = self.params["horario_abertura"]
        fecho = self.params["horario_fecho"]

        with open(path, newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                hora = str_to_minutos(row[0])
                nome = row[1]

                if hora < abertura or hora > fecho:
                    self.erros.append(
                        f"Passageiro {nome} ignorado (hora fora do horário: {row[0]})"
                    )
                    continue

                p = Passageiro(nome, hora)
                p.seguidos = []

                for s in row[2:]:
                    s = s.strip()
                    if s not in p.seguidos:
                        p.seguidos.append(s)

                self.passageiros.append(p)
                self.seguidores[p.nome] = p.seguidos

    def carregar_questoes_seguidores(self, path):
        with open(path, newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                self.questoes_seguidores.append((row[0].strip(), row[1].strip()))

    def carregar_viagens(self, path):
        abertura = self.params["horario_abertura"]
        fecho = self.params["horario_fecho"]

        with open(path, newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                hora = str_to_minutos(row[0])
                tipo = row[1]
                nif = row[2]
                comboio = row[3] if len(row) == 4 else None

                if hora < abertura or hora > fecho:
                    self.erros.append(
                        f"Viagem ignorada (fora do horário): {row[0]} {tipo}"
                    )
                    continue

                if tipo == "Chegada" and not comboio:
                    self.erros.append(
                        f"Chegada inválida às {row[0]} (comboio não identificado)"
                    )
                    continue

                self.viagens.append(Viagem(hora, tipo, nif, comboio))

        self.viagens = self.insertion_sort_key(
            self.viagens,
            lambda v: v.hora
        )


    def simular(self):
        bilheteira = Bilheteira(
            self.params["duracao_atendimento"],
            self.params["duracao_bilheteira_plataforma"]
        )

        # Passageiros ordenados por chegada à bilheteira
        fila_chegadas = Fila()
        for p in self.insertion_sort_key(self.passageiros, lambda p: p.chegada_bilheteira):
            fila_chegadas.enqueue(p)


        eventos = []
        tempo = self.params["horario_abertura"]

        # Vagas por partida
        vagas_viagem = {
            v.hora: self.params["numero_de_lugares_vip"]
            for v in self.viagens if v.tipo == "Partida"
        }

        movimentos = []  # (inicio, fim, comboio_id)

        # =========================
        # SIMULAÇÃO DA BILHETEIRA
        # =========================
        while not fila_chegadas.is_empty() or not bilheteira.is_empty():
            while not fila_chegadas.is_empty() and fila_chegadas.front().chegada_bilheteira <= tempo:
                bilheteira.adicionar(fila_chegadas.dequeue())

            p, novo_tempo = bilheteira.atender_proximo(tempo)

            if p:
                tempo = novo_tempo

                # atribuição de viagem
                viagem_atribuida = None
                for v in self.viagens:
                    if v.tipo == "Partida" and vagas_viagem.get(v.hora, 0) > 0:
                        if p.pronto_plataforma <= v.hora:
                            viagem_atribuida = v
                            break

                # sempre registamos a entrada (fim do atendimento) como evento —
                # mesmo que o passageiro não consiga bilhete e não tenha partida.
                if viagem_atribuida:
                    p.partida = viagem_atribuida.hora
                    vagas_viagem[viagem_atribuida.hora] -= 1

                    eventos.append((p.fim_atendimento, "entra", p))
                    eventos.append((p.partida, "sai", p))
                else:
                    # registar a entrada ao fim do atendimento (passageiro na plataforma sem partida)
                    eventos.append((p.fim_atendimento, "entra", p))
                    self.erros.append(
                        f"Passageiro {p.nome} não conseguiu bilhete para nenhuma viagem"
                    )
            else:
                # ninguém para atender → avançar tempo
                if not fila_chegadas.is_empty():
                    tempo = fila_chegadas.front().chegada_bilheteira

        # =========================
        # PROCESSAMENTO DAS VIAGENS
        # =========================
        for v in self.viagens:
            if v.tipo == "Chegada":
                entrada = v.hora - self.params["duracao_entrada_plataforma"]
                fim_desembarque = v.hora + self.params["duracao_desembarque"]
                chegada_parque = fim_desembarque + self.params["duracao_plataforma_parque"]

                # colisões
                for ini, fim, cid in movimentos:
                    if max(ini, entrada) < min(fim, chegada_parque):
                        self.erros.append(
                            f"Colisão entre o comboio {v.comboio} da chegada das {minutos_to_str(v.hora)} "
                            f"e o comboio {cid}"
                        )

                movimentos.append((entrada, chegada_parque, v.comboio))

                if self.parque.tamanho() >= self.params["capacidade_do_parque"]:
                    self.erros.append(
                        f"Parque cheio na chegada do comboio {v.comboio} às {minutos_to_str(v.hora)}"
                    )
                    continue

                self.parque.push(Comboio(v.comboio))

            elif v.tipo == "Partida":
                saida_parque = (
                    v.hora
                    - self.params["duracao_embarque"]
                    - self.params["duracao_plataforma_parque"]
                )
                chegada_saida = v.hora + self.params["duracao_entrada_plataforma"]

                for ini, fim, cid in movimentos:
                    if max(ini, saida_parque) < min(fim, chegada_saida):
                        self.erros.append(
                            f"Colisão entre o comboio {v.comboio or 'desconhecido'} "
                            f"da partida das {minutos_to_str(v.hora)} e o comboio {cid}"
                        )

                if self.parque.esta_vazia():
                    self.erros.append(
                        f"Não existem comboios disponíveis para efectuar a partida das {minutos_to_str(v.hora)}"
                    )
                    continue

                comboio = self.parque.pop()
                v.comboio = comboio.id
                movimentos.append((saida_parque, chegada_saida, v.comboio))

        # =========================
        # GERAÇÃO DO PLACAR
        # =========================

        def chave_evento(e):
            tempo, tipo, _ = e
            prioridade = 0 if tipo == "entra" else 1
            return (tempo, prioridade)
        
        eventos = self.insertion_sort_key(eventos, chave_evento)

        # snapshots de entradas cumulativas (após processar todas as 'entra' de cada hora)
        entrados = set()
        entradas = []
        i = 0
        while i < len(eventos):
            t = eventos[i][0]
            # processar todas as entradas neste tempo
            while i < len(eventos) and eventos[i][0] == t and eventos[i][1] == "entra":
                _, _, p = eventos[i]
                entrados.add(p.nome)
                i += 1
            if entrados:
                entradas.append((t, self.insertion_sort(list(entrados))))
            # pular saídas do mesmo tempo (não afetam o snapshot de entradas acumuladas)
            while i < len(eventos) and eventos[i][0] == t and eventos[i][1] == "sai":
                i += 1

        # snapshots de saídas baseados no conjunto final de quem entrou
        conjunto_final = set(entrados)
        partidas = self.insertion_sort_key([v for v in self.viagens if v.tipo == "Partida"], lambda v: v.hora)
        saidas = []
        for v in partidas:
            hora_partida = v.hora
            partiram_ate = {p.nome for p in self.passageiros if getattr(p, 'partida', None) is not None and p.partida <= hora_partida}
            restantes = self.insertion_sort(list(conjunto_final - partiram_ate))
            if restantes:
                saidas.append((hora_partida, restantes))

        # junta as entradas + saidas e sem duplicar por lista de nomes (ignora horários repetidos)
        combinado = entradas + saidas
        vistos = set()
        placar = []
        for t, nomes in combinado:
            chave = tuple(nomes)
            if chave in vistos:
                continue
            vistos.add(chave)
            placar.append((t, nomes))

        self.placar = placar


    def escrever_outputs(self, pasta):
        os.makedirs(pasta, exist_ok=True)

        with open(os.path.join(pasta, "erro.txt"), "w") as f:
            for e in self.erros:
                f.write(e + "\n")

        with open(os.path.join(pasta, "parque.csv"), "w", newline="") as f:
            csv.writer(f).writerows([[c.id] for c in self.parque.itens])

        with open(os.path.join(pasta, "viagens.csv"), "w", newline="") as f:
            w = csv.writer(f)
            for v in self.viagens:
                w.writerow([minutos_to_str(v.hora), v.tipo, v.nif, v.comboio])

        with open(os.path.join(pasta, "passageiros.csv"), "w", newline="") as f:
            w = csv.writer(f)
            for p in self.passageiros:
                w.writerow([
                    minutos_to_str(p.chegada_bilheteira),
                    p.nome,
                    minutos_to_str(p.partida) if p.partida else ""
                ])

        with open(os.path.join(pasta, "placar.csv"), "w", newline="") as f:
            w = csv.writer(f)
            # `self.placar` já contém listas ordenadas e sem duplicados; escrever diretamente.
            rows = (
                [minutos_to_str(t)] + list(nomes)
                for t, nomes in self.placar
                if t is not None and nomes
            )
            w.writerows(rows)

        with open(os.path.join(pasta, "questoes_seguidores.csv"), "w", newline="") as f:
            w = csv.writer(f)
            for seguidor, seguido in self.questoes_seguidores:
                w.writerow([
                    seguidor,
                    seguido,
                    seguidor in self.seguidores and seguido in self.seguidores[seguidor]
                ])
    
    def insertion_sort(self, lista):
        ordenada = lista[:]
        for i in range(1, len(ordenada)):
            chave = ordenada[i]
            j = i - 1
            while j >= 0 and ordenada[j] > chave:
                ordenada[j+1] = ordenada[j]
                j -= 1
            ordenada[j+1] = chave
        return ordenada
    
    def insertion_sort_key(self, lista, func_chave):
        ordenada = lista[:]
        for i in range(1, len(ordenada)):
            atual = ordenada[i]
            chave_atual = func_chave(atual)
            j = i - 1

            while j >= 0 and func_chave(ordenada[j]) > chave_atual:
                ordenada[j + 1] = ordenada[j]
                j -= 1

            ordenada[j + 1] = atual

        return ordenada
