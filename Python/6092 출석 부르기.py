a = list()

for i in range(24):
    a.append(0)
    
n = int(input())
nlist = input().split()

for i in range(n):
    a[int(nlist[i])] += 1
    
for i in range(1, len(a)):
    print(a[i], end=' ')
