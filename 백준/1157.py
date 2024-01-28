words = input().lower() #소문자로 저장
wlist = list(set(words))

cnt = []

for i in wlist:
    count = words.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")

else:
    print(wlist[(cnt.index(max(cnt)))].upper())
