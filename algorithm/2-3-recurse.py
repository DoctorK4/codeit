# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    length_n = len(str(n))
    
    if length_n-1 == 0 :
        return n
    
    else : 
        digit = n // (10 ** (length_n-1))
        next_digit = n - (digit * (10 ** (length_n-1)))
        total = digit + sum_digits(next_digit)
        return total

# 테스트 코드
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))