class CircularLinkedList(object):
    def __init__(self) -> None:
        self._head = None
        self._data = None
        self._next = None
        self._len = 0

    def set_head(self, head):
        self._head = head

    def get_head(self):
        return self._head

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def set_next(self, next):
        self._next = next

    def get_next(self):
        return self._next

    def set_len(self, val):
        self._len += val

    def __len__(self):
        return self._len

    def __repr__(self) -> str:
        return "<class 'CircularLinkedList'>"

    def __str__(self) -> str:   # Time complexity O(n)
        s = "["
        curr: CircularLinkedList = self.get_head()
        if curr is not None:
            s += f"{str(curr.get_data())}, "
            curr = curr.get_next()
            while curr != self.get_head():
                s += f"{str(curr.get_data())}, "
                curr = curr.get_next()
            s = s.rstrip()
            s += "]"
        else:
            s += "]"
        return s

    def clear(self):
        self.set_head(None)
        self.set_len(-len(self))

    def insert_head(self, data):    # Time complexity O(n)
        curr: CircularLinkedList = self.get_head()
        new_node = CircularLinkedList()
        new_node.set_data(data)
        new_node.set_next(new_node)

        if curr is not None:
            while curr.get_next() != self.get_head():
                curr = curr.get_next()
            curr.set_next(new_node)
            new_node.set_next(self.get_head())
            self.set_head(new_node)
            self.set_len(1)
        else:
            self.set_head(new_node)
            self.set_len(1)

    def insert_tail(self, data):    # Time complexity O(n)
        curr: CircularLinkedList = self.get_head()
        new_node = CircularLinkedList()
        new_node.set_data(data)
        new_node.set_next(new_node)
        if curr is not None:
            curr = curr.get_next()
            while curr.get_next() != self.get_head():
                curr = curr.get_next()
            new_node.set_next(self.get_head())
            curr.set_next(new_node)
            self.set_len(1)
        else:
            self.set_head(new_node)
            self.set_len(1)

    def insert(self, data, index):  # Time complexity O(n)
        curr: CircularLinkedList = self.get_head()
        if index < 0 or index > len(self):
            raise IndexError("Index out of range")
        elif index == 0:
            self.insert_head(data)
        elif index == len(self):
            self.insert_tail(data)
        else:
            new_node = CircularLinkedList()
            new_node.set_data(data)
            new_node.set_next(new_node)
            counter = 2
            curr = curr.get_next()
            while counter != index and curr.get_next() != self.get_head():
                curr = curr.get_next()
                counter += 1
            new_node.set_next(curr.get_next())
            curr.set_next(new_node)
            self.set_len(1)

    def delete_head(self):  # Time complexity O(n)
        if not self.get_head().get_data() or len(self) == 0:
            raise ValueError("Can not delete from empty list")
        else:
            curr = self.get_head().get_next()
            while curr.get_next() != self.get_head():
                curr = curr.get_next()
            head = curr.get_next()
            curr.set_next(head.get_next())
            self.set_head(head.get_next())
            self.set_len(-1)
            del head

    def delete_tail(self):  # Time complexity O(n)
        if not self.get_head().get_data() or len(self) == 0:
            raise ValueError("Can not delete from empty list")
        else:
            curr = self.get_head()
            while curr.get_next().get_next() != self.get_head():
                curr = curr.get_next()
            next = curr.get_next()
            curr.set_next(next.get_next())
            self.set_len(-1)
            del next

    def delete(self, index):    # Time complexity O(n)
        if index < 0 or index > len(self):
            raise IndexError("Index out of range")
        elif index == 0:
            self.delete_head()
        elif index == len(self):
            self.delete_tail()
        else:
            curr = self.get_head()
            counter = 0
            while curr.get_next() != self.get_head() and counter != index-1:
                counter += 1
                curr = curr.get_next()
            del_item = curr.get_next()
            curr.set_next(curr.get_next().get_next())
            self.set_len(-1)
            del del_item

    def get(self, index):
        if not self.get_head().get_data() or len(self) == 0:
            return None
        elif index == 0:
            return self.get_head().get_data()
        else:
            counter = 0
            curr = self.get_head()
            while curr.get_next() != self.get_head() and counter != index:
                counter += 1
                curr = curr.get_next()
            return curr.get_data()

    def search(self, data):
        if not self.get_head().get_data() or len(self) == 0:
            return []
        else:
            curr = self.get_head()
            res = []
            while curr.get_next() != self.get_head():
                if curr.get_data() == data:
                    res.append(curr.get_data())
                curr = curr.get_next()
            return res


if __name__ == "__main__":
    cl = CircularLinkedList()
    cl.insert_head(1)
    cl.insert_head(2)
    cl.insert_head(3)
    print(
        f"Circular linked list after insertion at head {str(cl)} with length {str(len(cl))}")
    cl.insert_tail(4)
    cl.insert_tail(5)
    cl.insert_tail(6)
    print(
        f"Circular linked list after insertion at tail {str(cl)} with length {str(len(cl))}")
    cl.insert(100, 0)
    cl.insert(200, len(cl))
    cl.insert(300, 3)
    cl.insert(400, 6)
    print(
        f"Circular linked list after insertion at any index {str(cl)} with length {str(len(cl))}")
    cl.delete_head()
    cl.delete_head()
    print(
        f"Circular linked list after deleting at the head {str(cl)} with length {str(len(cl))}")
    cl.delete_tail()
    cl.delete_tail()
    print(
        f"Circular linked list after deleting at the tail {str(cl)} with length {str(len(cl))}")
    cl.delete(0)
    cl.delete(5)
    cl.delete(2)
    print(
        f"Circular linked list after deleting any index {str(cl)} with length {str(len(cl))}")
    print(cl.get(2))
    print(cl.search(1))
    cl.insert_head(1)
    print(cl.search(1))
    cl.clear()
    print(f"After clearing the list {str(cl)} with length {str(len(cl))}")
