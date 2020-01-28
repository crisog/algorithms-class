import time


# Esta es la clase que define la cola
# En este caso, la cola solo cuenta con una lista de elementos y dos funciones.
class Queue:
    def __init__(self):
        self.items = []

    # Esta función es para encolar elementos.
    def enqueue(self, item):
        self.items.insert(0, item)

    # Esta función es para desencolar elementos.
    def dequeue(self):
        return self.items.pop()

    # Esta función devuelve el tamaño de la cola.
    def size(self):
        return len(self.items)


q1 = Queue()

# Esta variable indica la cantidad de elementos que serán añadidos a cola.
element_count = 100001

print('Encolando...')
for x in range(1, int(element_count)):
    q1.enqueue(x)
    print('Elemento ', x, ' encolado.')

print('Desencolando...')
for x in range(1, q1.size()+1):
    q1.dequeue()
    print('Elemento ', x, ' desencolado.')
