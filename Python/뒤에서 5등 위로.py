arr = list(map(int, input().split()))

for i in range(5):
    minnum= min(arr)
    arr.remove(minnum)


arr.sort()
print(arr)