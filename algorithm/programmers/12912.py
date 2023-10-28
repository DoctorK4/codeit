def solution(a, b):
    #   두 수가 같은 경우
    if a == b:
        return a
#   두 수가 다른 경우
#   a가 b보다 큰 경우
    if a > b:
        addNum = b
        while addNum < a:
            addNum += 1
            b += addNum
        return b

    if a < b:
        addNum = a
        while addNum < b:
            addNum += 1
            a += addNum
        return a
