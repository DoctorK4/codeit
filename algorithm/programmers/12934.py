from math import sqrt

def solution(n):
    x = sqrt(n)
    if x == int(x):
        return (x+1)**2
    else:
        return -1