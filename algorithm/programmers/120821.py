def solution(num_list):
    answer = []
    while len(num_list) != 0:
        answer.append(num_list.pop(-1))
    return answer