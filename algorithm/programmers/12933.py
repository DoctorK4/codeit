def solution(n):
    n = str(n)
    arr = []
    
    for num in n:
        arr.append(num)
        
    arr.sort(reverse=True)