def solution(n):
    # 높이가 n인 삼각형을 담을 수 있는 배열
    matrix = [[0] * n for _ in range(n)]
    t = n * (n+1) // 2 
    x = y = angle = 0
    
    # 방향 설정
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    
    for i in range(1, t+1):
        matrix[y][x] = i
        
        # 비교를 위한 셋팅
        ny = y + dy[angle]
        nx = x + dx[angle]
        
        # 정상 진행
        if 0 <= ny < n and 0 <= nx < n and matrix[ny][nx] == 0:
            x, y = nx, ny
            
        # 방향 바꾸기 
        else:
            angle = (angle + 1) % 3
            y += dy[angle]
            x += dx[angle]   
    
    one = [y for x in matrix for y in x]
    answer = []
    for item in one:
        if item != 0:
            answer.append(item)
    
    return answer