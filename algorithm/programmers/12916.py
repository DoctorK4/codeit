def solution(s):
    s = s.lower()
    p_count = 0
    y_count = 0
    for letter in s:
        if letter == 'p':
            p_count += 1
        if letter == 'y':
            y_count += 1 
    
    if p_count == 0 and y_count == 0:
        return True
    return p_count == y_count