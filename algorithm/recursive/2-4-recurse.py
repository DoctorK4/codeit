# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    
    if len(some_list) > 1 :
        last = some_list[len(some_list)-1]
        some_list.pop()
        return [ last ] + flip(some_list)
    
    if len(some_list) == 1 or len(some_list) == 0 :
        return some_list

# 테스트 코드
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)
