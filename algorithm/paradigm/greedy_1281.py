def min_coin_count(value, coin_list):
    # 반복문 안쓰기
    # unit_500 = value // coin_list[1]
    # unit_100 = (value % coin_list[1]) // coin_list[0]
    # unit_50 = ((value % coin_list[1]) % coin_list[0]) // coin_list[3]
    # unit_10 = (((value % coin_list[1]) % coin_list[0]) % coin_list[3]) // coin_list[2]
    # return unit_500 + unit_100 + unit_50 + unit_10
    
    # 리스트 내림차순 정렬
    coin_list.sort(reverse=True)
    
    # 반복문 사용
    total = 0
    money = value
    for i in range(0, len(coin_list)):
        unit = money // coin_list[i]
        total += unit
        money = money % coin_list[i]
    
    return total

# 테스트 코드
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))