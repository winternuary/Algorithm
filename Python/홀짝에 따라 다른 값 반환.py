n = int(input())
result=0

if n % 2==1:
    for i in range(1, n+1):
        if i % 2 == 1:
            result += i
    print(result)

else:
    for i in range(1, n+1):
        if i % 2 == 0:
            result += i**2
    print(result)
