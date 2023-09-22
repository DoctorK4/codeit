def solution(rows, columns, queries):
    matrix = [[i * columns + (j+1) for j in range(columns)] for i in range(rows)]
    result = []
    for x1, y1, x2, y2 in queries:
        result.append(rotate(x1-1, y1-1, x2-1, y2-1, matrix))
    return result

def rotate(x1, y1, x2, y2, matrix):
    first = matrix[x1][y1]
    min_value = first
    # 왼쪽
    for j in range(x1, x2):
        matrix[j][y1] = matrix[j+1][y1]
        min_value = min(min_value, matrix[j+1][y1])
        
    # 아래
    for i in range(y1, y2):
        matrix[x2][i] = matrix[x2][i+1]
        min_value = min(min_value, matrix[x1][i+1])

    # 오른쪽
    for l in range(x2, x1, -1):
        matrix[l][y2] = matrix[l-1][y2]
        min_value = min(min_value, matrix[l-1][y2])
    
    # 위
    for k in range(y2, y1, -1):
        matrix[x1][k] = matrix[x1][k-1]
        min_value = min(min_value, matrix[x2][k-1])
        
    matrix[x1][y1+1] = first
    
    return min_value

        