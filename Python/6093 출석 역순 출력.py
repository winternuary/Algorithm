n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

for i in range(n-1, -1, -1): #역순으로 반복
  print(a[i], end=' ')
