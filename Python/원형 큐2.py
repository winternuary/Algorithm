def createCircularQueue(capacity=5):
    queue = [None] * capacity
    front = 0
    rear = 0

    def isEmpty():
        return front == rear

    def isFull():
        return front == (rear + 1) % capacity

    def enqueue(item):
        nonlocal rear
        if not isFull():
            rear = (rear + 1) % capacity
            queue[rear] = item

    def dequeue():
        nonlocal front
        if not isEmpty():
            front = (front + 1) % capacity
            return queue[front]

    def peek():
        if not isEmpty():
            return queue[(front + 1) % capacity]

    return enqueue, dequeue, peek


enqueue, dequeue, peek = createCircularQueue()
enqueue(1)
print(dequeue())
