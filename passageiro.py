class Passageiro:
    def __init__(self, nome, chegada):
        self.nome = nome
        self.chegada_bilheteira = chegada
        self.inicio_atendimento = None
        self.fim_atendimento = None
        self.pronto_plataforma = None
        self.partida = None
        self.seguidos = set()