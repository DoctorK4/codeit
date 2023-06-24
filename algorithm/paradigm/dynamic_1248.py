# Tabulation 접근
def fib_tab(n):
    fib_table = [0, 1, 1]
    for i in range (3, n + 1) :
        fib_i = fib_table[i - 1] + fib_table[i - 2]
        fib_table.append(fib_i)
        i += 1
    return fib_table[n]

# 테스트 코드
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))