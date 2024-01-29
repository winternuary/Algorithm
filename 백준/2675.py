n = int(input())

for _ in range(n):
    R, S = input().split()
    for j in S:
        print(j*int(R), end="")
    print()
