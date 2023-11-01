stack_size = 5
list = [None] * stack_size
top = -1

def isEmpty():
    return top == -1

def isFull():
    return top == stack_size - 1

def push(e):
    global top
    if not isFull():
        top += 1
        list[top] = e
    else:
        print("스택이 가득 참")


def pop():
    global top
    if not isEmpty():
        print(list[top])
        top = top-1

def peek():
    if not isEmpty():
        print(list[top])
    else:
        print("스택이 비었다")


