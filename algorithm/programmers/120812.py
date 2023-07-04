def solution(array):
    memo = {}
    for i in range(0, len(array)):
        if not array[i] in memo:
            memo[array[i]] = 1
        else:
            memo[array[i]] += 1
    tmp = [k for k,v in memo.items() if max(memo.values()) == v]
    if len(tmp) == 1:
        return tmp[0]
    else:
        return -1

# 생각해본 로직
# 1. 메모를 위한 빈 딕셔너리를 생성
# 2. 반복문을 통해 array의 각 요소들을 평가
# 2-1. memo의 key값으로 있는 요소는, value값을 +1 
# 2-2. memo의 key값에 없는 요소는, value 1을 가진 새로운 key값을 생성
# 3. 평가가 끝나고나면, memo의 key값들 중 가장 큰 value를 가진 값들을 return
# 4. 복수의 값이라면, -1을 return