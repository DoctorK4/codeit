def solution(n):
    n = str(n)
    arr = []
    
    for num in n:
        arr.append(int(num))
        
    arr.sort(reverse=True)
    answer = ""
    for num in arr:
        answer += str(num)
    
    return int(answer)