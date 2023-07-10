import math

def solution(price):
    if 100000 <= price < 300000:
        discount_rate = 0.05
    elif 300000 <= price < 500000:
        discount_rate = 0.1
    elif 500000 <= price <= 1000000:
        discount_rate = 0.2
    else:
        discount_rate = 0
    return math.trunc(price * (1-discount_rate))