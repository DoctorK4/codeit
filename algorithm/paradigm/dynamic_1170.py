def max_profit_memo(price_list, count, cache):
    # base case
    if count < 2:
        return price_list[count]
    
    # 저장된 캐시 값이 있는 경우
    if count in cache:
        return cache[count]
        
    # 저장된 캐시 값이 없는 경우
    temp_list = []

    if count < len(price_list):
        temp_list.append(price_list[count])
    
    for i in range(1, count // 2 + 1):
        profit = max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count-i, cache)
        temp_list.append(profit)
    
    # 캐시에 새로 기록
    cache[count] = max(temp_list)
    return cache[count]
        
def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)

print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))

# 로직은 어느 정도 거의 유추를 했던 것 같다. 
# 포인트 1 : 반복문 범위 지정에 있어서 count // 2 + 1로 일괄적으로 할 수 있는 것을 짝.홀수 구분으로 어렵게 갔던 부분이 아쉬웠다. 
# 포인트 2 : max_profit_memo(i)를 count-i와 결합되는 부분 로직은 잘 생각해냈다. 
# 포인트 3 : count 크기에 따른 temp_list 요소는 생각해보지 못했던 부분이었다. 이 부분을 생각하지 못해 포인트 1에서 짝.홀수 분기처리를 했던 것 같다. 