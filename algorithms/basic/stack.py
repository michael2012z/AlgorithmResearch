class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    s = Stack()
    s.push('a')
    s.push('b')
    s.push(1)
    s.push(2)
    while s.size() > 0:
        print(s.pop())

        
