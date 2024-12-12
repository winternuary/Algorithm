number, n, m = map(int, input().split())
result=0
if number % n == 0 and number % m == 0:
    result=1
    print(result)
else:
    result=0
    print(result)
