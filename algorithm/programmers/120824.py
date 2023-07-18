def solution(num_list):
    # 1. 반복문을 통해 리스트의 요소들을 검사
    # 2. 검사 결과에 따라 answer[0]과 [1]의 값을 새로 지정
    answer = [0, 0]
    for item in num_list:
        if item % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    
    return answer