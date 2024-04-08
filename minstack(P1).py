class MinStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.min_stack = []

    def is_full(self):
        return len(self.stack) == self.capacity

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        if self.is_full():
            print("Stack overflow!!")
        else:
            self.stack.append(item)
            if len(self.min_stack) == 0 or item <= self.min_stack[-1]:
                self.min_stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack underflow!!")
        else:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self):
        if self.is_empty():
            print("Top doesn't exist")
        else:
            print("Smallest element is : " + str(self.min_stack[-1]))
            print("Top is : " + str(self.stack[-1]))

    def display(self):
        if self.is_empty():
            print("Stack is empty!!")
        else:
            print(self.stack)


a = MinStack(3)
a.push(32)
a.push(68)
a.push(24)
a.push(12)
a.display()
a.top()
a.pop()
a.display()
a.top()