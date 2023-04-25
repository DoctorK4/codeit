def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    # 반복문

    while start_index < end_index :
        mid_point = (start_index + end_index ) // 2
        
        # 중간값과 같은 경우
        if element == some_list[mid_point]:
            return mid_point
            
        # 중간값보다 큰 경우
        elif element > some_list[mid_point]:
            start_index = mid_point + 1
        
        elif element < some_list[mid_point]:
            end_index = mid_point - 1 
        
    return None

# 테스트 코드
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))