def 몰라(A):
    if not A:
        return 0
    else:
        return A.pop() + 몰라(A)

A = list(map(int, input().split()))
result = 몰라(A)
print(f"{result}")
