def solution(n):
    answer = 0
    # 약수 구하기 
    # 1부터 n까지 n을 나눠을 때 나머지가 0인 친구들
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    
    return answer