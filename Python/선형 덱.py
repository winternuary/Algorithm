class Deque:
    def __init__(self):
        self.MAX_Deque = 5            # 덱의 최대 크기
        self.front = -1               # 덱의 맨 앞 포인터
        self.rear = self.MAX_Deque    # 덱의 맨 뒤 포인터
        self.list = [None] * self.MAX_Deque  # 덱을 저장할 리스트

    def isEmpty(self):
        # 덱이 비어있는지 확인
        if self.rear == self.MAX_Deque and self.front == -1:
            return True
        else:
            return False

    def isFull(self):
        # 덱이 가득 차 있는지 확인
        if self.front == self.MAX_Deque - 1 or self.rear == 0:
            return True
        else:
            return False

    def AddFront(self, item):
        # 덱의 맨 앞에 요소 추가
        if not self.isFull():
            self.front += 1
            self.list[self.front] = item
        else:
            print("덱이 가득 찼습니다.")

    def DeleteFront(self):
        # 덱의 맨 앞에서 요소 제거
        if not self.isEmpty():
            data = self.list[self.front]
            self.list[self.front] = None
            self.front -= 1
            return data
        else:
            print("덱이 비어 있습니다.")

    def GetFront(self):
        # 덱의 맨 앞 요소 반환
        return self.list[self.front]

    def AddRear(self, item):
        # 덱의 맨 뒤에 요소 추가
        if not self.isFull():
            self.rear -= 1
            self.list[self.rear] = item
        else:
            print("덱이 가득 찼습니다.")

    def DeleteRear(self):
        # 덱의 맨 뒤에서 요소 제거
        if not self.isEmpty():
            data = self.list[self.rear]
            self.list[self.rear] = None
            self.rear += 1
            return data
        else:
            print("덱이 비어 있습니다.")

    def GetRear(self):
        # 덱의 맨 뒤 요소 반환
        return self.list[self.rear]
