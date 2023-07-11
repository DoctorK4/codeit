# 다른 사람 답안 참고
# def solution(progresses, speeds):
#     ans=[]

#     # 경과시간
#     time = 0
    
#     # 배포 기능 수
#     cnt = 0
    
#     while len(progresses) > 0:
#         if progresses[0] + time * speeds[0] >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             cnt += 1
#         else:
#             if cnt > 0:
#                 ans.append(cnt)
#                 cnt = 0
#             time += 1
    
#     ans.append(cnt)

#     return ans

from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    times = deque()

    for i in range(len(progresses)):
        # math.ceil 사용 안하면 테스트케이스 통과 못함 정수단위로 프로세스 처리가 되어야하기 때문
        time = math.ceil((100 - progresses[i]) / speeds[i])
        times.append(time)

    while times:
        left = times.popleft()
        result = 1
        while len(times) != 0 and left >= times[0]:
            result += 1
            times.popleft()
        answer.append(result)
        
    return answer


# 내가 생각한 로직
# from collections import deque

# def solution(progresses, speeds):
#     # 배포 갯수 리스트
#     answer = []

#     # 완료에 소요되는 시간 리스트
#     times = deque()
    
#     # 1. 각 작업에 소요되는 시간 구하기
#     # times 구하기
#     for i in range(len(progresses)):
#         time = math.ceil((100 - progresses[i]) / speeds[i])
#         times.append(time)

#     # 6. 2 ~ 5 를 progresses List의 갯수가 0이 될때까지 반복
#     while len(progresses) > 0:
#         elapsed_time = times.popleft()
        
#         # 2. times에서 popleft한 값을 progresses에 반영
#         for i in range(len(progresses)):
#             # 2-1. progresses 각 요소들에 elapsed_time * speeds한 값을 더한다. 
#             progresses[i] = progresses[i] + (elapsed_time * speeds[i])

#         # 3. progresses에서 100 이상 숫자 갯수 세기 
#         over_100 = 0
#             # 3-1. progresses 각 요소를 맨앞에서부터 100 이상인지 검사
#         if progresses[0] >= 100:
#             # 3-2. 100 이상이라면 progresses list에서 빼내고, over_100에 1 추가
#             while len(progresses) > 0 and progresses[0] >= 100:
#                 progresses.pop(0)
#                 speeds.pop(0)
#                 over_100 += 1
        
#         # 4. 갯수(over_100)를 answer list에 추가
#         answer.append(over_100)

#         # 5. progresses의 갯수와 times의 갯수가 동일해질때까지 times.popleft()
#         while len(progresses) != len(times):
#             times.popleft()

#     return answer

# 테스트
print(solution([93, 30, 55], [1, 30, 5]))

# 테스트 1
# [93, 30, 55] [1, 30, 5]
# 완료까지 필요한 시간 리스트
# times = [7, 3, 9]

# 7일 후
# [100, 100, 90] [2]

# 경과시간과 완료에 필요한 시간 리스트 비교
# 같거나 작은 것의 갯수를 answer 리스트에 추가

# 2일 후 (9 - 경과시간)
# [100, 100, 100] [2, 1]


# 테스트 2
# 5일 후
# [100, 95, 100, 100, 85, 100] [1,]

# 5일 후
# [100, 100, 100, 100, 90, 100] [1, 3]

# 10일 후
# [100, 100, 100, 100, 100, 100] [1, 3, 2]