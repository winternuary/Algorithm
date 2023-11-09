class CircularQueue:
    def __init__(self, capacity=5):
        self.capacit = capacity
        self.list = [None]*capacity
        self.front = 0
        self.rear = 0
    
    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front ==  (self.rear+1) % self.capacit
    
    def enqueue(self,item):
        if not self.isFull():
            self.rear = (self.rear+1) %  self.capacit
            self.list[self.rear] = item


    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % self.capacit
            return self.list[self.front]

def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1) % self.capacit]

Q = CircularQueue()
Q.enqueue(1)

print(Q.dequeue())
