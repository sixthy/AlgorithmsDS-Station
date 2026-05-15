# Pilha (LIFO) - Utilizada no parque de comboios.
class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if self.esta_vazia():
            print("Lista vazia!")
            return None
        return self.itens.pop()

    def top(self):
        if self.esta_vazia():
            print("Lista vazia!")
            return None
        return self.itens[-1]

    def esta_vazia(self):
        return self.itens == []

    def tamanho(self):
        return len(self.itens)
