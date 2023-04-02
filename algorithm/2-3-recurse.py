# n의 각 자릿수의 합을 리턴
def sum_digits(n):
  length_n = int(len(str(n)))
    
  if n-1 < 0 :
    return 
    
  else : 
    digit = n / (10 ** (length_n - 1))
    total_digit = digit + sum_digits(n - (digit * (10 ** (length_n - 1))))
    return total_digit

# 테스트 코드
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))