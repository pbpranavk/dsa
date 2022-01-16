class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("Invalid previous node")
            return

        new_node = Node(new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def search(self, x):
        current = self.head

        while current is not None:
            if current.data == x:
                return True

            current = current.next

        return False

    def delete_node(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def delete_node_at_position(self, position):
        if self.head is None:
            return

        if position == 0:
            self.head = self.head.next
            return self.head

        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == position:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1

        prev.next = temp
        return prev

    def delete_list(self):
        current = self.head
        while current:
            prev = current.next

            del current.data

            current = prev

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end= " ")
            temp = temp.next
        print()

    def get_length(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next
        return count

llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)
llist.print_list()
llist.delete_node(1)
llist.print_list()
llist.delete_node_at_position(2)
llist.print_list()
# llist.delete_list()
# llist.print_list()
print(llist.get_length())
print(llist.search(2))
print(llist.search(22))