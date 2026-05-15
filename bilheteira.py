# Bilheteira (Fila FIFO de atendimento aos passageiros).
class Bilheteira:
    def __init__(self, dur_atendimento, dur_desloc):
        self.fila = []
        self.dur_atendimento = dur_atendimento
        self.dur_desloc = dur_desloc

    def adicionar(self, passageiro):
        self.fila.append(passageiro)

    def remover(self):
        if self.is_empty():
            return None
        return self.fila.pop(0)
    
    def is_empty(self):
        return len(self.fila) == 0

    def atender_proximo(self, hora_atual):
        if not self.fila:
            return None, hora_atual

        p = self.remover()
        p.inicio_atendimento = max(hora_atual, p.chegada_bilheteira)
        p.fim_atendimento = p.inicio_atendimento + self.dur_atendimento
        p.pronto_plataforma = p.fim_atendimento + self.dur_desloc
        return p, p.fim_atendimento
