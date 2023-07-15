def solution(my_string):
    # 1. my_string의 마지막 값부터 임시 배열에 추가
    i = -1
    temp = []
    while len(my_string) != len(temp):
        temp.append(my_string[i])
        i -= 1
    total = ""
    for item in temp:
        total += item
    answer = total
    return answer

# 다른 사람 풀이

# def solution(my_string):
#     answer = ''

#     for i in range(len(my_string)-1, -1, -1) :
#         answer += my_string[i]
#     return answer