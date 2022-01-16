class Node:
    def __init__(self):
        self.data = None
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        temp = Node()
        temp.data = value

        if (self.front == None):
            self.front = temp
        else:
            self.rear.next = temp

        self.rear = temp
        self.rear.next = self.front

    def dequeue(self):
        if (self.front == None):
            print("Queue is empty")
            return -999999999999

        value = None
        if (self.front == self.rear):
            value = self.front.data
            self.front = None
            self.rear = None
        else:
            temp = self.front
            value = temp.data
            self.front = self.front.next
            self.rear.next = self.front

        return value

    def display(self):
        temp = self.front

        print("Elements in Circular Queue are: ", end = " ")

        while (temp.next != self.front):
            print(temp.data, end = " ")
            temp = temp.next

        print(temp.data)

q = Queue()
q.enqueue(14)
q.enqueue(22)
q.enqueue(6)
q.display()
print(f"Deleted value = {q.dequeue()}")
print(f"Deleted value = {q.dequeue()}")
q.display()
q.enqueue(9)
q.enqueue(20)
q.display()