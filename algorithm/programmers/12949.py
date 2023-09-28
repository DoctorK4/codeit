def solution(arr1, arr2):
    # m * n 행렬
    m = len(arr1)
    # n = len(arr1[0])
    
    # k * l 행렬
    # k = len(arr2)
    l = len(arr2[0])
    
    # 결과물 = m * l 행렬
    answer = [[0 for _ in range(l)] for _ in range(m)] 
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                   answer[i][j] += arr1[i][k] * arr2[k][j]           
        
    return answer