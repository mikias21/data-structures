class SingleLinkedList(object):
    def __init__(self) -> None:
        self.data = None
        self.next = None
        self.head = None
        self.length = 0

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def get_last(self):  # Time complexity O(n)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        return curr.data

    def is_empty(self):
        return self.head is None and self.length == 0

    def has_next(self):
        return self.next != None

    def clear(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):  # Time complexity O(n)
        rep = "["
        curr = self.head
        while curr.next != None:
            rep += f"{str(curr.data)}, "
            curr = curr.next
        rep += f"{str(curr.data)}"
        rep += "]"
        return rep

    def insert_beginning(self, data):  # Time complexity O(1)
        new = SingleLinkedList()
        new.set_data(data)
        if self.is_empty():  # Check if the head is none and set new node as head
            self.head = new
            self.head.next = None
        else:
            new.next = self.head
            self.head = new
        self.length += 1

    def insert_end(self, data):  # Time complexity O(n)
        new = SingleLinkedList()
        new.set_data(data)
        if self.is_empty():
            self.head = new
            self.head.next = None
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new
            new.next = None
        self.length += 1

    def insert_pos(self, data, idx):        # Time complexity O(n)
        if idx < 0 or idx > self.length:
            raise IndexError("The given index is out of bounds")

        if self.is_empty():
            print("List is empty, item insert at the beggining")
            self.insert_beginning(data)
        elif idx == self.length:
            self.insert_end(data)
        elif idx == 0:
            self.insert_beginning(data)
        else:
            new = SingleLinkedList()
            new.set_data(data)
            counter = 2
            curr = self.head
            while counter != idx:  # Loop until the index given is found
                curr = curr.next
                counter += 1
            new.next = curr.next
            curr.next = new
            self.length += 1

    def delete_beginning(self):  # Time complexity O(1)
        if self.is_empty():
            raise Exception("Can not delete from empty list.")
        else:
            curr = self.head
            self.head = curr.next
            self.length -= 1
            del curr

    def delete_end(self):  # Time complexity O(n)
        if self.is_empty():
            raise Exception("Can not delete from empty list.")
        else:
            curr = self.head
            while curr.next.next != None:
                curr = curr.next
            next = curr.next
            curr.next = None
            del next
            self.length -= 1

    def delete_pos(self, idx):  # Time complexity O(n)
        if idx < 0 or idx > self.length:
            raise IndexError("Given index out of bounds.")
        if idx == 0:
            self.delete_beginning()
        if idx == self.length:
            self.delete_end()
        else:
            counter = 2
            curr = self.head
            while counter != idx:
                curr = curr.next
                counter += 1
            next = curr.next
            curr.next = curr.next.next
            self.length -= 1
            del next

    def get(self, idx):  # Time complexity O(n)
        if idx < 0 or idx > self.length:
            raise IndexError("Given index out of bounds.")
        elif idx == 0:
            return self.head.data
        elif idx == self.length:
            return self.get_last()
        else:
            counter = 1
            curr = self.head
            while counter != idx:
                curr = curr.next
                counter += 1
            return curr.data

    def search(self, data):  # Time complexity O(n)
        found = []
        curr = self.head
        index = 0
        while curr.next != None:
            if curr.data == data:
                found.append(index)
            curr = curr.next
            index += 1

        if curr.data == data:
            found.append(index)

        return found


if __name__ == "__main__":
    ll1 = SingleLinkedList()
    ll1.insert_beginning(1)
    ll1.insert_beginning(2)
    ll1.insert_beginning(3)
    print("After insert at beggining operation: ", ll1)
    ll1.insert_end(4)
    ll1.insert_end(5)
    ll1.insert_end(6)
    print("After insert at end operation: ", ll1)
    ll1.insert_pos(100, 3)
    ll1.insert_pos(200, len(ll1))
    ll1.insert_pos(300, 0)
    print("After insert at any position operation: ", ll1)
    print("Length of the list: ", len(ll1))
    ll1.delete_beginning()
    print("After deleting from beginning: ", ll1)
    print("Length of the list: ", len(ll1))
    ll1.delete_end()
    print("After deleting from end: ", ll1)
    print("Length of the list: ", len(ll1))
    ll1.delete_pos(3)
    print("After deleting from any index: ", ll1)
    print("Length of the list: ", len(ll1))
    print(ll1.get(0))
    print(ll1.get(len(ll1)))
    print(ll1.get(4))
    ll1.insert_beginning(6)
    ll1.insert_end(6)
    ll1.insert_pos(6, 3)
    print(ll1)
    print(ll1.search(6))
    ll1.clear()
    print(len(ll1))
