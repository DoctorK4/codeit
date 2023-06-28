def sum_digits(n):
    string = str(n)
    total = 0
    for i in range (0, len(string)):
        total += int(string[i])
        i += 1
    return total
    

# 테스트 코드
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))