#방법1
def solution(num_list):
    answer = []
    for i in range(5):
        min_sum = min(num_list)  # 리스트에서 최소값 찾기
        answer.append(min_sum)  # 최소값을 answer 리스트에 추가
        num_list.remove(min_sum)  # 최소값을 리스트에서 제거
        answer.sort
    return answer
