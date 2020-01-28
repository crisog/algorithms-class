
from datetime import datetime
import random
import time


# Esta clase define el tipo de elementos en la cola.
# En este caso, cuentan con dos atributos: valor y prioridad.
class Node():
    def __init__(self, value=0, priority=0):
        self.value = value
        self.priority = priority


# Esta clase define la cola tomando en cuenta la prioridad.
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # Esta función verifica si la cola está vacia.
    def is_empty(self):
        return len(self.queue) == []

    # Esta función es para encolar elementos.
    def enqueue(self, Node):
        self.queue.append(Node)

    # Esta función es para desencolar elementos (mayor prioridad, sale primero)
    def dequeue(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i].priority > self.queue[max].priority:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

    # Esta función devuelve el tamaño de la cola.
    def size(self):
        return len(self.queue)


# Esta variable indica la cantidad de elementos que serán añadidos a cola.
element_count = 100000

myQueue = PriorityQueue()
for x in range(1, int(element_count)):
    random.seed(datetime.now())
    # Los valores solo van de 1 a 100
    value = random.randrange(1, 101)
    # La prioridad máxima es 5
    priority = random.randrange(1, 6)
    print(x, 'Encolando elemento con valor:', value, 'y prioridad:', priority)
    myQueue.enqueue(Node(value, priority))

# Desencolando hasta que la lista quede vacía.
for x in range(1, myQueue.size()+1):
    e = myQueue.dequeue()
    print(x, "Desencolando elemento con valor:",
          e.value, "y prioridad:", e.priority)

print('La cola ha sido terminada.')
