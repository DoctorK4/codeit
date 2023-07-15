def solution(s):
    answer = []
    for i in range(0, len(s)):
        if len(answer) == 0:
            if s[i] == "(":
                answer.append(s[i])
            else:
                return False
        else:
            if s[i] == ")":
                answer.pop()
            else:
                answer.append(s[i])
                
    if len(answer) == 0:
        return True
    else:
        return False
    
    
    # 1. 반복문을 통해 s의 각 요소들을 검사
    """
    2. 검사 로직
    사용할 자료구조 - 스택
    추가 - append
    빼기 - pop
    "("를 만났을 경우 : append
    ")"를 만났을 경우 : pop
    
    """
    # 3. 최종적으로 스택의 길이가 0이면 true, 그렇지 않으면 false