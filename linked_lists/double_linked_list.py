class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.next = None
        self.prev = None
        self.data = None
        self.length = 0

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def setPrev(self, prev):
        self.prev = prev

    def getPrev(self):
        return self.prev

    def setData(self, data):
        self.data = data

    def __len__(self):
        return self.length

    def __str__(self):  # TimeComplexity O(n)
        strr = "["
        curr = self.head
        while curr.next != None:
            strr += f"{curr.data}, "
            curr = curr.next
        strr += f"{curr.data}"
        strr += "]"
        return strr

    # Insert operations
    def insert_head(self, data):    # TimeComplexity O(1)
        new_node = DoubleLinkedList()
        new_node.setData(data)
        if self.head is None and self.length == 0:
            self.head = new_node
            self.head.next = None
            self.head.prev = None
            self.length += 1
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def insert_tail(self, data):    # TimeComplexity O(n)
        new_node = DoubleLinkedList()
        new_node.setData(data)
        if self.head is None or self.length == 0:
            self.head = new_node
            self.head.next = None
            self.head.prev = None
            self.length += 1
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            new_node.next = None
            new_node.prev = curr
            curr.next = new_node
            self.length += 1

    def insert(self, data, pos):    # Time complexity O(n)
        if pos < 0 or pos > self.length:
            raise ValueError("The given position is invalid")
        elif pos == 0:
            self.insert_head(data)
        elif pos == self.length:
            self.insert_tail(data)
        else:
            new_node = DoubleLinkedList()
            new_node.setData(data)
            curr = self.head
            prev = None
            counter = 1
            while curr.next != None and counter != pos:
                prev = curr
                curr = curr.next
                counter += 1

            new_node.next = curr
            new_node.prev = prev
            curr.prev = new_node
            prev.next = new_node
            self.length += 1

    # Delete operations
    def delete_head(self):  # TimeComplexity O(1)
        if self.head is None or self.length == 0:
            raise ValueError("Can not delete from empty list")
        else:
            if self.length == 1:
                curr = self.head
                self.head.next = None
                self.length = 0
                del curr
            else:
                curr = self.head
                self.head = self.head.next
                self.head.prev = None
                self.length -= 1
                del curr

    def delete_tail(self):  # Time complexity O(n)
        if self.head is None or self.length == 0:
            raise ValueError("Can not delete from empty list")
        else:
            if self.length == 1:
                curr = self.head
                self.head.next = None
                self.length = 0
                del curr
            else:
                curr = self.head
                while curr.next.next != None:
                    curr = curr.next
                curr.next = None
                self.length -= 1

    def delete(self, pos):  # Time complexity O(n)
        if pos < 0 or pos > len(self):
            raise IndexError("Index out of range")
        if pos == 0 or pos == 1:
            self.delete_head()
        elif pos == self.length:
            self.delete_tail()
        else:
            counter = 1
            curr = self.head
            prev = None
            while curr.next != None and counter != pos:
                prev = curr
                curr = curr.next
                counter += 1
            prev.next = curr.next
            curr.next.prev = prev
            del curr
            self.length -= 1

    def get(self, index):   # Time complexity O(n)
        if index < 0 or index > len(self):
            raise IndexError("Index out of range")
        if index == 0:
            return self.head.data
        counter = 1
        curr = self.head
        while curr != None and counter != index:
            counter += 1
            curr = curr.next
        return curr.data

    def search(self, val):
        res_idx = []
        curr = self.head
        counter = 0
        while curr != None:
            if curr.data == val:
                res_idx.append(counter)
            curr = curr.next
            counter += 1
        return res_idx


if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.insert_head(1)
    dll.insert_head(2)
    dll.insert_head(3)
    print(f"After inserting at the head {dll} of length {len(dll)}")
    dll.insert_tail(4)
    dll.insert_tail(5)
    dll.insert_tail(6)
    print(f"After inserting at the tail {dll} of length {len(dll)}")
    dll.insert(100, 0)
    dll.insert(200, len(dll))
    dll.insert(300, 3)
    print(f"After inserting at any given index {dll} of length {len(dll)}")
    dll.delete_head()
    dll.delete_head()
    print(f"After delete at head {dll} of length {len(dll)}")
    dll.delete_tail()
    dll.delete_tail()
    print(f"After delete at tail {dll} of length {len(dll)}")
    dll.delete(0)
    dll.delete(len(dll))
    print(f"After deleting using index {dll} of length {len(dll)}")
    dll.delete(2)
    print(f"After deleting using index {dll} of length {len(dll)}")
    print(dll.get(len(dll)))
    print(dll.get(0))
    dll.insert_tail(2)
    dll.insert(2, 2)
    dll.insert(2, 0)
    print(dll.search(2))
    print(dll)
