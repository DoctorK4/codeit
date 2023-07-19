# 나의 풀이
# 로직
# 1부터 까지 반복
# 1. 가장 작은 2번째 값을 가진 튜플을 찾는다. 이를 a라고 한다. 
# 2-1. answer list의 길이가 0이라면 바로 해당 튜플을 course_list로부터 pop하여 answer list에 추가
# 2-2. 만일, answer list의 길이가 0보다 크다면, 
#  answer 리스트의 마지막 요소의 2번째 값보다 a의 첫 번째 값이 더 큰 지 확인한다. 
# 3-1. a의 첫번째 값보다 크다면, 해당 튜플을 course_list로부터 pop하여 answer list에 추가
# 3-2. 그렇지않다면 course_list에서부터 pop만 함. 

def course_selection(course_list):
    answer = []
    while len(course_list) != 0:
        min_value = float('inf')  # 최솟값을 저장하기 위한 변수를 무한대로 초기화
        min_tuple = None  # 최솟값을 가진 튜플을 저장하기 위한 변수
        
        for tuple_item in course_list:
            if tuple_item[1] < min_value:
                min_value = tuple_item[1]
                min_tuple = tuple_item
        min_index = course_list.index(min_tuple)
        
        if len(answer) != 0:
            if answer[-1][1] < min_tuple[0]:
                answer.append(min_tuple)
        else:
            answer.append(min_tuple)
        
        course_list.pop(min_index)
    
    return answer

# 모범답안
def course_selection(course_list):
    # 수업을 끝나는 순서로 정렬한다
    sorted_list = sorted(course_list, key=lambda x: x[1])

    # 가장 먼저 끝나는 수업은 무조건 듣는다
    my_selection = [sorted_list[0]]

    # 이미 선택한 수업과 안 겹치는 수업 중 가장 빨리 끝나는 수업을 고른다
    for course in sorted_list:
        # 마지막 수업이 끝나기 전에 새 수업이 시작하면 겹친다
        if course[0] > my_selection[-1][1]:
            my_selection.append(course)