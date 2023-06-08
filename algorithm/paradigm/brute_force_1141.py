def trapping_rain(buildings):
    rain = []
    
    for i in range(len(buildings)):
        if i == 0 or i == len(buildings)-1:
            rain.append(0)
            continue
        else :     
            left = max(buildings[:i])
            right = max(buildings[i:])
            if left > buildings[i] and right > buildings[i]:
                water = min(left, right) - buildings[i]
            else :
                water = 0
            rain.append(water)
    
    total = 0
    for i in rain:
        total = total + i
    return total
    
    
# 테스트 코드
print(trapping_rain([3, 0, 0, 2, 0, 4])) # 0, 3, 3, 1, 3 = 10
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])) 