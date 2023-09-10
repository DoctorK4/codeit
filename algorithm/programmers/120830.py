def solution(n, k):
    sheep = n * 12000
    drink = (k-(n//10)) * 2000
    return sheep + drink
