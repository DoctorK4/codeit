def find_same_number(some_list):
    memo = []
    for i in range(0, len(some_list)):
        if some_list[i] in memo:
            return some_list[i]
        else:
            memo.append(some_list[i])

# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))