def sum_digits(n):
    string_n = str(n)
    # total = 0
    # for i in range (0, len(string)):
    #     total += int(string[i])
    #     i += 1
    # return total
    # 재귀로 풀기
    if len(string_n) == 1 :
        return n
    elif len(string_n) > 1 :
        return sum_digits(int(string_n[:-1])) + sum_digits(int(string_n[-1]))

# 테스트 코드
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))