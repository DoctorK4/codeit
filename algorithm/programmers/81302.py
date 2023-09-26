def solution(places):
    return [check(place) for place in places]

def check(place):
    for idx_row, row in enumerate(place):
        for idx_col, cell in enumerate(row):
            if cell != "P":
                continue
            isNotEndRow = idx_row != 4
            isNotEndCol = idx_col != 4
            
            isNotFourthRow = idx_row < 3
            isNotFourthCol = idx_col < 3
            
            isNotFirstCol = idx_col != 0
            
            # cell이 P라면
            if isNotEndRow:
                # - 밑이 P (단, 마지막 행이 아니어야 함)
                if place[idx_row + 1][idx_col] == "P":
                    return 0
                # - 밑의 밑이 P (단, 4번째 행이 아니어야 함) & 그 사이가 X가 아니라면
                if isNotFourthRow:
                    if place[idx_row + 2][idx_col] == "P" and place[idx_row+1][idx_col] != "X":
                        return 0
                # - 왼쪽과 밑이 x가 아닌 왼쪽 아래 대각선 P (마지막 행이 아니고, 첫번째 열이 아니어야한다. )
                if isNotFirstCol:
                    if place[idx_row+1][idx_col-1] == "P": 
                        if place[idx_row+1][idx_col] != "X" or place[idx_row][idx_col-1] != "X":
                            return 0
                # - 오른쪽과 밑이 x가 아닌 오른쪽 아래 대각선 P (마지막 행이 아니고, 마지막 열이 아니어야한다.  )
                if isNotEndCol:
                    if place[idx_row+1][idx_col+1] == "P":
                        if place[idx_row][idx_col+1] != "X" or place[idx_row+1][idx_col] != "X":
                            return 0
                
            if isNotEndCol:
                # - 오른쪽이 P 단, 마지막 열이 아니어야 함)
                if place[idx_row][idx_col+1] == "P":
                    return 0
                # - 오른쪽의 오른쪽이 P (단, 4번째 열이 아니어야함) & 그 사이가 X가 아니라면
                if isNotFourthCol:
                    if place[idx_row][idx_col+2] == "P":
                        if place[idx_row][idx_col+1] != "X" or place[idx_row][idx_col+1] == "P":
                            return 0
            
    return 1
    
    # 거리두기 준수 => 1, 준수 X => 0
    # 맨해튼 거리가 1일 때 
        # - 밑이 P (단, 마지막 행이 아니어야 함)
        # - 오른쪽이 P (단, 마지막 열이 아니어야 함)
    # 맨해튼 거리가 2일 때 
        # - 왼쪽과 밑이 x가 아닌 왼쪽 아래 대각선 P (마지막 행이 아니고, 첫번째 열이 아니어야한다. )
        # - 오른쪽과 밑이 x가 아닌 오른쪽 아래 대각선 P (마지막 행이 아니고, 마지막 열이 아니어야한다.  )
        # - 밑의 밑이 P (단, 4번째 행이 아니어야 함)
        # - 오른쪽의 오른쪽이 P (단, 4번째 열이 아니어야함)
