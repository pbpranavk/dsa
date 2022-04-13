import queue


class Queue:
    def __init__(self, c):
        self.queue = []
        self.front = self.rear = 0
        self.capacity = c

    def enqueue(self, data):
        if self.capacity == self.rear:
            print("\nQueue is full")
        else:
            self.queue.append(data)
            self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print("\nQueue is empty")
        else:
            x = self.queue.pop(0)
            self.rear -= 1

    def display(self):
        if self.front == self.rear:
            print("\nQueue is empty")
        else:
            for i in self.queue:
                print(i, " <-- ", end="")

    def get_front(self):
        if self.front == self.rear:
            print("\nQueue is empty")
        else:
            print(f"\n{self.queue[self.front]} is the front element")

q = Queue(4)
q.display()

# Inserting elements in the queue
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

# Print queue elements
q.display()

# Insert element in queue
q.enqueue(60)

# Print queue elements
q.display()
q.dequeue()
q.dequeue()

# Print queue elements
print("\n\nafter two node deletion\n")
q.display()

# Print front of queue
q.get_front()
