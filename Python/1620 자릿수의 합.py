n = int(input())
len = len(str(n))

sum = 0
num = n

for i in range(1, len+1):
    sum = sum + num % 10
    num = int(num / 10)

while sum >= 10:
    new_sum = 0
    while sum > 0:
        new_sum += sum % 10
        sum = int(sum / 10)
    sum = new_sum

print(sum)
