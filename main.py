import csv
from estacao import Estacao
from tempo import str_to_minutos

def ler_parametros(path):
    params = {}
    with open(path, newline="") as f:
        for p, v in csv.reader(f):
            if p == "localizacao_do_problema":
                continue
            params[p] = str_to_minutos(v) if ":" in v else int(v)
    return params

def main():
    base = "Input/Problema1"
    out = "Output/Problema1"

    params = ler_parametros(f"{base}/parametros.csv")
    estacao = Estacao(params)

    estacao.carregar_parque(f"{base}/parque.csv")
    estacao.carregar_viagens(f"{base}/viagens.csv")
    estacao.carregar_passageiros(f"{base}/passageiros.csv")
    estacao.carregar_questoes_seguidores(f"{base}/questoes_seguidores.csv")

    estacao.simular()
    estacao.escrever_outputs(out)

if __name__ == "__main__":
    main()
