def solution(lottos, win_nums):
    answer = []
    count = 0

    temp = lottos[:]
    for i in range(len(temp)):
        if temp[i] == 0:
            temp[i] = win_nums[i]
        if temp[i] in win_nums:
            count += 1

    if count == 6:
        answer.append(1)
    elif count == 5:
        answer.append(2)
    elif count == 4:
        answer.append(3)
    elif count == 3:
        answer.append(4)
    elif count == 2:
        answer.append(5)
    else:
        answer.append(6)

    count = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count += 1

    if count == 6:
        answer.append(1)
    elif count == 5:
        answer.append(2)
    elif count == 4:
        answer.append(3)
    elif count == 3:
        answer.append(4)
    elif count == 2:
        answer.append(5)
    else:
        answer.append(6)

    return answer
