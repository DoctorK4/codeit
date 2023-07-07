def solution(slice, n):
    i = 1
    while (slice*i) // n < 1:
        i += 1
    return i