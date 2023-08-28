def select_stops(water_stops, capacity):
    min_point = 0
    max_point = min_point+capacity
    answer = []
    for i in range(0, len(water_stops)):
        # 마지막 원소인 경우
        if i == len(water_stops) - 1:
            answer.append(water_stops[i])
        # max_point보다 다음에 올 인덱스 원소가 큰 경우
        elif water_stops[i+1] > max_point:
            answer.append(water_stops[i])
            max_point = water_stops[i] + capacity
        # max_point보다 다음에 올 인덱스 원소가 작은 경우
        elif water_stops[i+1] <= max_point:
            continue
    
    return answer

# 테스트 코드
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))