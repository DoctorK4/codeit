from collections import deque

def solution(n):
    answer = []
    queue = deque()
    for letter in str(n):
        queue.append(int(letter))
        
    while queue:
        answer.append(queue.pop())
        
    return answer