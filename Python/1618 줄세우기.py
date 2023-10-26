li = list(map(int, input().split()))

min= min(li)
max = max(li)
rest = sum(li) - min - max

print(min,rest,max)

#min,max함수를 사용해서 꼭 만들고 싶었는데
#나머지 숫자를 어떻게 해줘야할지 몰랐었다.
#그냥 세 수의 합에서 나머지 숫자빼고 빼주면 되능구나...
