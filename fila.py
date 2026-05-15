class Fila:
    def __init__(self):
        self.elements = []

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.elements.pop(0)
        return None

    def front(self):
        if not self.is_empty():
            return self.elements[0]
        return None
    
    def tail(self):
        if not self.is_empty():
            return self.elements[-1]
        return None

    def is_empty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)