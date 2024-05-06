a = []

for _ in range(10):
    num = int(input())
    sum = num % 42
    a.append(sum)

result = set(a)
print(len(result))
