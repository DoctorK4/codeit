# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    temp_list = []
    # 반복문으로 모든 짝들을 자료구조 (x, y, distance(x,y)) 형태로 만들어 임시리스트에 넣어버리고 
    for i in coordinates:
        for j in coordinates:
            if i != j:
                reverse_value = (j, i, distance(j, i))
                if reverse_value in temp_list:
                    continue
                else :
                    temp_list.append((i, j, distance(i, j)))
    
    # 각 튜플의 2번 값끼리 중 최솟값을 찾고
    distance_list = []
    for i in temp_list:
        distance_list.append(i[2])
    
    min_index = distance_list.index(min(distance_list))
    
    # 그 최솟값의 1, 2번 값을 리턴해준다. 
    return [temp_list[min_index][0], temp_list[min_index][1]] 
    
# 테스트 코드
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))