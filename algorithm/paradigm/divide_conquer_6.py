def merge(list1, list2):
    merged_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    if len(list1) == i:
        merged_list = merged_list + list2[j:]
        return merged_list

    if len(list2) == j:
        merged_list = merged_list + list1[i:]
        return merged_list
    
# 합병 정렬
def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list
    else:
        half1 = my_list[0:len(my_list)//2]
        half2 = my_list[len(my_list)//2:]
        return merge(merge_sort(half1), merge_sort(half2))
    
# 테스트 코드
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))