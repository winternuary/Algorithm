def solution(n):
    three = ""
    answer = 0
    
    while n > 0:
        three += str(n % 3)
        n = n // 3
        
    for i in range(len(three)):
        answer += int(three[i]) * (3 ** (len(three) - 1 - i))

        
    return answer
