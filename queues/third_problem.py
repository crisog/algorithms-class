from datetime import datetime
import random
import time
import threading


class Node():
    def __init__(self, value=0, priority=0):
        self.value = value
        self.time = 0
        self.priority = priority


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def is_empty(self):
        return len(self.queue) == []

    def enqueue(self, Node):
        Node.time = time.time()
        self.queue.append(Node)

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

    def size(self):
        return len(self.queue)

    # La prioridad aumenta en 1 cada 10 segundos.
    def anti_starvation(self):
        t = threading.Timer(10, self.anti_starvation)
        for i in range(len(self.queue)):
            if(self.queue[i].priority < 5):
                self.queue[i].priority += 1
        return t


n_elements = input(
    'Introduzca la cantidad de elementos aleatorios a encolar: ')
myQueue = PriorityQueue()
t = myQueue.anti_starvation()
t.start()
for x in range(1, int(n_elements)):
    random.seed(datetime.now())
    # Valor entre 1 y 100
    value = random.randrange(1, 101)
    # Máxima prioridad 5
    priority = random.randrange(1, 6)
    print('Encolando', x, 'elemento con valor:',
          value, 'y prioridad:', priority)
    myQueue.enqueue(Node(value, priority))
    time.sleep(0.1)

while not myQueue.is_empty():
    i = 1
    e = myQueue.dequeue()
    print("Desencolando", i, "elemento con valor:", e.value, "y prioridad:",
          e.priority, ". Estuvo en cola por:", round(time.time() - e.time, 1), "segundos.")
    i += 1
    time.sleep(0.1)
t.stop()
