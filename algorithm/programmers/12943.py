def solution(num):
    count = 0
    while num != 1:
        count += 1
        if count == 500:
            return -1
        if num % 2 == 0:
            num = num // 2
            continue
        if num % 2 == 1:
            num = num * 3 + 1
            continue
    return count
