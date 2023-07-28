def solution(n):
    answer = 0
    string = str(n)
    for letter in string:
        answer += int(letter)
    return answer