n = int(input())
result = 0

for i in range(1, n+1):
  result = result + i

for i in range(1, n+1):
  for j in range(i):
    print(result, end=" ")
    result = result -1
  print()
