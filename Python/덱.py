class MyDeque:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.front = 0
        self.rear = 0
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size

    def AddFront(self, item):
        if not self.isFull():
            self.front = (self.front - 1) % self.max_size
            self.items[self.front] = item
            self.size += 1

    def DeleteFront(self):
        if not self.isEmpty():
            item = self.items[self.front]
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return item

    def GetFront(self):
        if not self.isEmpty():
            return self.items[self.front]

    def AddRear(self, item):
        if not self.isFull():
            self.items[self.rear] = item
            self.rear = (self.rear + 1) % self.max_size
            self.size += 1

    def DeleteRear(self):
        if not self.isEmpty():
            self.rear = (self.rear - 1) % self.max_size
            item = self.items[self.rear]
            self.size -= 1
            return item
    
    def GetRear(self):
        if not self.isEmpty():
            return self.items[(self.rear - 1) % self.max_size]


# 덱 테스트
my_deque = MyDeque(5)

my_deque.AddRear(1)
my_deque.AddRear(2)
my_deque.AddFront(3)
my_deque.AddFront(4)

print("덱의 프론트", my_deque.GetFront())  # 출력: Front of the deque: 4
print("덱의 끝", my_deque.GetRear())    # 출력: Rear of the deque: 2

my_deque.deleteFront()  # 4 삭제

print("프론트 요소 삭제", my_deque.DeleteFront())  # 출력: Deleted front element: 3
print("끝 요소 삭제", my_deque.DeleteRear())    # 출력: Deleted rear element: 2

print("덱의 사이즈", my_deque.size)  # 출력: Size of the deque: 1
