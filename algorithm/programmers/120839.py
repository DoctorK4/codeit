def solution(rsp):
    win_case = {
        '2':'0', 
        '0':'5', 
        '5':'2'
    }
    answer = []
    for case in rsp:
        answer.append(win_case[case])
    
    return ''.join(answer)