def power(x, y):
    # O(N^2)
    # if y == 1:
    #     return x
    # elif y > 1:
    #     return power(x, y - 1) * x
    # O(logN)
    # if y == 0:
    #     return 1
    # if y == 1: 
    #     return x
    # elif y > 0:
    #     # 짝수인 경우
    #     if y % 2 == 0:
    #         return power(x, y / 2 ) * power(x, y / 2 )
    #     # 홀수인 경우
    #     elif y % 2 == 1:
    #         return power(x, y//2) * power(x, (y//2)+1)
  # 모범 답안
  if y == 0:
      return 1

  # 계산을 한 번만 하기 위해서 변수에 저장
  subresult = power(x, y // 2)
      
  # 문제를 최대한 똑같은 크기의 문제 두 개로 나눠준다 (짝수, 홀수 경우 따로)
  if y % 2 == 0:
      return subresult * subresult
  else:
      return x * subresult * subresult

        

# 테스트 코드
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))