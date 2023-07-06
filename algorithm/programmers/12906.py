def solution(arr):
    answer = []
    for i in range(0, len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i-1] != arr[i]:
            answer.append(arr[i])
    return answer

# 핵심 로직 : 이전 값과 다른 값일 경우, 정답배열에 추가한다. 