MAX = 100

class Deque:
    def __init__(self, size):
        self.arr = [0] * MAX
        self.front = -1
        self.rear = 0
        self.size = size

    def is_full(self):
        return ((self.front == 0 and self.rear == self.size-1) or
                self.front == self.rear + 1)

    def is_empty(self):
        return self.front == -1

    def insert_front(self,key):
        if self.is_full():
            print("Overflow")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front = self.front - 1

        self.arr[self.front] = key

    def insert_rear(self, key):
        if self.is_full():
            print("Overflow")
            return

        if (self.front == -1):
            self.front = 0
            self.rear = 0
        elif (self.rear == self.size-1):
            self.rear = 0
        else:
            self.rear = self.rear+1
        self.arr[self.rear] = key

    def delete_front(self):
        if self.is_empty():
            print("Queue underflow")
            return

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            if self.front == self.size - 1:
                self.front = 0
            else:
                self.front = self.front + 1

    def delete_rear(self):
        if self.is_empty():
            print("Queue underflow")
            return

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear = self.rear - 1

    def get_front(self):
        if (self.is_empty()):
            print("Underflow")
            return -1

        return self.arr[self.front]

    def get_rear(self):
        if(self.is_empty() or self.rear < 0):
            print("Underflow")
            return -1

        return self.arr[self.rear]

dq = Deque(5)
dq.insert_rear(5)
dq.insert_rear(10)
print(f"Rear element : {dq.get_rear()}")
dq.delete_rear()
print(f"Rear become : {dq.get_rear()}")
dq.insert_front(15)
print(f"Front element: {dq.get_front()}")
dq.delete_front()
print(f"Front become : {dq.get_front()}")
