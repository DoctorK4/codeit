def min_fee(pages_to_print):
    
    # 1. 오름차순 정렬
    pages_to_print.sort()
    
    # 2. 개인별 벌금금액 더하기
    total = 0
    for i in range(1, len(pages_to_print)+1):
        for j in range(0, i):
            total += pages_to_print[j]    
        
    return total


# 테스트 코드
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
