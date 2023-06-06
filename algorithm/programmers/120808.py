import math

def solution(numer1, denom1, numer2, denom2):
  # 맞는 풀이
  numer = numer1 * denom2 + numer2 * denom1
  denom = denom1 * denom2

  gcd = math.gcd(denom, numer)
  
  return [ numer/gcd, denom/gcd ]

  # 기존 틀렸던 풀이
  # lcm = 0
  # for i in range (max(denom1, denom2), (denom1*denom2)+1):
  #     if i%denom1 == 0 and i%denom2 == 0:
  #         lcm = i
  #         break      
  # answer = [numer1*(lcm//denom1)+numer2*(lcm//denom2) , lcm]
  # return answer
