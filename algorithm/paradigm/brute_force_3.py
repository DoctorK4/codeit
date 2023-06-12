def max_product(left_cards, right_cards):
    temp_list = []
    # 1. 반복문을 통해 left_cards의 각 요소들을 추출 
    for i in left_cards:
        for j in right_cards:
    # 2. 추출한 각 요소들에 right_cards의 각 요소들 값을 추출하여 곱해준다. 
            multiplied_value = i * j
    # 3. 곱해준 값을 temp_list에 넣어주고
            temp_list.append(multiplied_value)
    # 4. 반복문이 종료되면 temp_list에서 가장 큰 값을 return 해준다. 
    return max(temp_list)
    
# 테스트 코드
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))