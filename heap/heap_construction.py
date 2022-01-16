#TODO: Redo this
from heapq import heappush, heappop, heapify

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) / 2

    def insert_key(self, k):
        heappush(self.heap, k)

    def decrease_key(self, i, new_val):
        self.heap[i] = new_val
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]

    def extract_min(self):
        return heappop(self.heap)

    def delete_key(self, i):
        self.decrease_key(i, float("-inf"))
        self.extract_min()

    def get_min(self):
        return self.heap[0]

heapObj = MinHeap()
heapObj.insert_key(3)
heapObj.insert_key(2)
heapObj.delete_key(1)
heapObj.insert_key(15)
heapObj.insert_key(5)
heapObj.insert_key(4)
heapObj.insert_key(45)

print(heapObj.extractMin())
print(heapObj.getMin())
heapObj.decreaseKey(2, 1)
print(heapObj.getMin())
