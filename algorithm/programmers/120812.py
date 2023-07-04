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
# 3. 평가가 끝나고나면, memo의 요소 중 최댓값과 같은 값들을 리스트로 담음
# 4. 리턴한 리스트의 길이가 1이라면, 해당 요소를 return, 길이가 1 이상이라면 최댓값이 복수이므로, -1을 return

# 활용한 문법
# 리스트 컴프리핸션
# for 변수명 in 기존 리스트 if 조건문