def max_profit(price_list, count):
    profit_table = [0]
    if count == 0:
        return profit_table[0]

    for i in range(1, count+1):
          temp = []
        # 이미 해당 갯수의 단일 판매 가격이 있는 경우
          if i < len(price_list):
            price = price_list[i]
        # 단일 판매 가격이 없어 경우의 수 중 최대값을 구해야하는 경우    
          else:
              price = 0
          temp.append(price)
          for j in range(1, i//2 + 1):
              temp.append(profit_table[j] + profit_table[i - j])
          answer = max(temp)
          profit_table.append(answer)
        
    return profit_table[count]
    
# 테스트 코드
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
