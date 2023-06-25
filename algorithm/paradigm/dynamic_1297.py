# 주제 : 피보나치 수열 공간 최적화

# 모범 답안
def fib_optimized2(n):
    prev = 0
    curr = 1
    for i in range (1, n):
        prev, curr = curr, prev + curr
    return curr

# 처음 내가 짠 코드
def fib_optimized(n):
    previous = 0
    current = 1
    i = 0
    while i < n-1 :
        temp_prev = previous
        previous = current
        current = previous + temp_prev
        i += 1
    return current

# 테스트 코드
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
