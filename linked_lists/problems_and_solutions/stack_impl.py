class Stack(object):
    def __init__(self) -> None:
        self._head = None
        self._data = None
        self._next = None
        self._length = 0

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

    def __len__(self):
        return self._length

    def clear(self):
        self.set_head(None)

    def __repr__(self) -> str:
        return "class <'stack'>"

    def __str__(self):
        s = "[ "
        curr = self.get_head()
        if len(self) > 0:
            while curr.get_next() != None:
                s += f"{str(curr.get_data())}, "
                curr = curr.get_next()
            s += f"{str(curr.get_data())}, "
            s += "]"
            return s
        else:
            return "[]"

    def push(self, data):
        new_node = Stack()
        new_node.set_data(data)
        if len(self) == 0:
            self.set_head(new_node)
            self._length += 1
        else:
            new_node.set_next(self.get_head())
            self.set_head(new_node)
            self._length += 1

    def pop(self):
        if len(self) == 0:
            raise ValueError("can not pop from empty stack")
        elif len(self) == 1:
            head = self.get_head().get_data()
            self.clear()
            self._length = 0
            return head
        else:
            curr = self.get_head()
            self.set_head(curr.get_next())
            self._length -= 1
            val = curr.get_data()
            del curr
            return val


if __name__ == '__main__':
    stack = Stack()
    print(f"Initial stack of length {len(stack)} and values {stack}")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(
        f"after pushing 3 items into stack of length {len(stack)} and values {stack}")
    print(stack.pop())
    print(stack.pop())
    print(
        f"after poping 2 items into stack of length {len(stack)} and values {stack}")
