def solution(x):
#   1. 수의 각 자릿수를 하나하나씩 분리한다.
    lst = list(str(x))
    print(lst)
#   2. 분리한 숫자들을 다 더한다.
    total = 0
    for digit in lst:
        total += int(digit)
    print(total)
#   3. 더한 숫자를 x로 나눠서 나머지가 0인지 여부를 Return한다. 
    return (x % total == 0)