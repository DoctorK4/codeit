def solution(num_list, n):
    answer = []
    unit = len(num_list) // n # 4
    count = [i for i in range(0, n)]
    
    for j in range(0, len(num_list), n):
        bundle = []
        for i in range(0, n):
            bundle.append(num_list[j + i])
        answer.append(bundle)
    return answer