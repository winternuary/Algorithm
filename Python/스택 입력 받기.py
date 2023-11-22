class Stack:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.list = [None] * capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.list[self.top] = e
        else:
            print("스택이 가득 참")

    def pop(self):
        if not self.isEmpty():
            print(self.list[self.top])
            self.top -= 1
        else:
            print("스택이 비었다")

    def peek(self):
        if not self.isEmpty():
            print(self.list[self.top])
        else:
            print("스택이 비었다")

    def input_push(self):
        e = input("입력할 값을 입력하세요: ")
        self.push(e)


stack = Stack()

stack.input_push()
stack.input_push()
stack.input_push()


stack.pop()
stack.pop()
stack.pop()
