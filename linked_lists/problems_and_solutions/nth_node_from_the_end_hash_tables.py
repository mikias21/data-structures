class LinkedList(object):
    def __init__(self) -> None:
        self.head = None
        self.next = None
        self.data = None
        self.length = 0

    def set_head(self, head):
        self.head = head

    def get_head(self):
        return self.head

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def __len__(self):
        return self.length

    def __str__(self) -> str:
        curr = self.head
        s = "["
        while curr.next != None:
            s += f"{str(curr.data)}, "
            curr = curr.next
        s += f"{str(curr.data)}"
        s += "]"
        return s

    def insert_head(self, data):
        new_node = LinkedList()
        new_node.data = data
        if len(self) == 0:
            self.head = new_node
            self.length += 1
        else:
            new_node.set_next(self.head)
            self.head = new_node
            self.length += 1

    def find_n_node_from_end(self, n):
        list_vals = {}
        pos = 0
        curr = self.head
        if len(self) == 0:
            raise ValueError("Can not traverse empty list")
        elif n < 0 or n > len(self):
            raise IndexError("Given n value out of range")
        else:
            while curr.next != None:
                list_vals[pos] = curr.data
                pos += 1
                curr = curr.next
            list_vals[pos] = curr.data
        return list(list_vals.values())[pos - n]


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_head(4)
    ll.insert_head(17)
    ll.insert_head(1)
    ll.insert_head(5)
    print(ll)
    print(ll.find_n_node_from_end(3))
