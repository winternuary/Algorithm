arr = list(map(int, input().split()))
deleteArr = list(map(int, input().split()))


result = [x for x in arr if x not in deleteArr]
print(result)