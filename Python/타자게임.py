import random
import time

word_list = [
    "I love you.",
    "I must eat fast food because I'm so hungry.",
    "Coding is so difficult.",
    "Wow... you are so beautiful"
]

random.shuffle(word_list)

print("게임을 시작합니다. (종료하려면 'exit' 입력)")

for sentence in word_list:
    start_time = time.time()
    
    correct_count = 0
    typo_count = 0

    user_input = input(sentence + '\n')

    if user_input.lower() == 'exit':
        print("게임을 종료 합니다.")
        break

    # 타자 속도, 정확도, 오타율 계산
    sentence_length = len(sentence)
    user_input_length = len(user_input)

    min_length = min(sentence_length, user_input_length)

    for i in range(min_length):
        if sentence[i] == user_input[i]:
            correct_count += 1
        else:
            typo_count += 1

    correct_count += max(0, sentence_length - user_input_length)
    
    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\n정확도: {:.2f}%".format((correct_count / sentence_length) * 100))
    print("오타율: {:.2f}%".format((typo_count / sentence_length) * 100))
    print("타자 속도: {:.2f}초\n".format(elapsed_time))

else:
    print("모든 문장을 입력하여 게임을 종료합니다.")

