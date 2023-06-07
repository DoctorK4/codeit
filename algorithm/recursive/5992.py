def triangle_number(n):
    # 여기에 코드를 작성하세요
    if n == 1:
        return 1
    elif n > 1:
        return n + triangle_number(n-1)

# 테스트 코드
for i in range(1, 11):
    print(triangle_number(i))