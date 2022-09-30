class LinkedList(object):
    def __init__(self) -> None:
        self.head = None
        self.data = None
        self.next = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self) -> str:
        s = "["
        curr = self.head
        while curr.next != None:
            s += f"{str(curr.data)}, "
            curr = curr.next
        s += f"{str(curr.data)}]"
        return s

    def insert(self, data):
        new_node = LinkedList()
        new_node.data = data
        if len(self) == 0:
            self.head = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def find_from_end(self, n):
        if n < 0 or n > len(self):
            raise IndexError("Index out of range")

        temp = self.head
        counter = 0
        while counter < n and temp.next != None:
            temp = temp.next
            counter += 1

        if counter < n or temp == None:
            return None

        nth = self.head
        while temp.next != None:
            temp = temp.next
            nth = nth.next

        return nth.data


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)
    print(ll)
    print(ll.find_from_end(3))
