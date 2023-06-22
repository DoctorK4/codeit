# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    input_list = [ my_list[index1], my_list[index2] ]
    my_list[index1] = input_list[1]
    my_list[index2] = input_list[0]
    return my_list

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    b = start
    i = start
    pivot = end
    while i < pivot:
        if my_list[i] < my_list[pivot]:
            swap_elements(my_list, b, i)
            b += 1
        i += 1
    swap_elements(my_list, b, pivot)
    pivot = b
    return pivot 

# 퀵 정렬 (start, end 파라미터 없이도 호출이 가능하도록 수정해보세요!)
def quicksort(my_list, start=0, end=None):
    if end == None:
        end = len(my_list)-1
    if end - start < 1:
        return
    pivot_index = partition(my_list, start, end)
    quicksort(my_list, start, pivot_index-1)
    quicksort(my_list, pivot_index+1, end)
    
# 테스트 코드 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 코드 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 코드 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)