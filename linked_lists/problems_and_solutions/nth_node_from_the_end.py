class LinkedList(object):
    def __init__(self) -> None:
        self.head = None
        self.data = None
        self.next = None
        self.prev = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self) -> str:
        curr = self.head
        if len(self) == 0:
            return "[]"
        else:
            s = "["
            curr = self.head
            while curr.next != None:
                s += f"{curr.data}, "
                curr = curr.next
            s += f"{curr.data}]"
            return s

    def insert(self, data):
        new_node = LinkedList()
        new_node.data = data
        if self.length == 0:
            self.head = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    def find_tail(self):
        if len(self) == 0:
            raise ValueError("can not traverse empty list")
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            return tail

    def find_n_from_end(self, n):
        if n > self.length:
            raise ValueError("fewer number of nodes")
        else:
            tail = self.find_tail()
            # Traverse backward
            counter = 1
            while tail != self.head and counter != n:
                tail = tail.prev
                counter += 1
            return tail.data


if __name__ == '__main__':
    ls = LinkedList()
    ls.insert(1)
    ls.insert(2)
    ls.insert(3)
    ls.insert(4)
    ls.insert(5)
    print(ls)
    print(ls.find_n_from_end(2))
