# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    input_list = [ my_list[index1], my_list[index2] ]
    my_list[index1] = input_list[1]
    my_list[index2] = input_list[0]
    return my_list
    

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    b = 0
    i = 0
    pivot = my_list[-1]
    for i in range (end - start + 1):
        if my_list[i] < pivot:
            swap_elements(my_list, b, i)
            b += 1
        elif i == end - start:
            swap_elements(my_list, b, i)
            return b
        i += 1


# 테스트 코드 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 코드 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
