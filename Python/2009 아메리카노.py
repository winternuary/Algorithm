a, b = map(int, input().split())


sum = int(a / b)
num = a - sum * b
num = num + sum

while num >= b:
    re = int(num/b)
    sum = sum + re
    num = num - b*re
    num = num + re

print(int(sum))
