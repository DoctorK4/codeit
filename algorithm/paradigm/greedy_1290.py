def min_fee(pages_to_print):
    
    # 1. 오름차순 정렬
    pages_to_print.sort()
    
    # 2. 개인별 벌금금액 더하기
    total = 0

    # 처음 작성했던 풀이 => 반복문 중첩으로 효율 떨어짐
    # for i in range(1, len(pages_to_print)+1):
    #     for j in range(0, i):
    #         total += pages_to_print[j]    
    
    # 곱셈을 활용한 합계금액 구하기
    for i in range(len(pages_to_print)):
        total += pages_to_print[i] * (len(pages_to_print)-i)
    return total


# 테스트 코드
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
