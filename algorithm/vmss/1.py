# 문제
"""
N명의 사람이 모여 스터디를 진행하기로 했다. 스터디에 참여하는 사람은 1번부터 N 번까지의 번호가 붙어있다.
스터디는 기본적으로 K일 동안 연속해서 진행되는데, 
만약 특정 날짜에 참석하지 못하는 인원이 전체 스터디 인원의 절반 이상이라면 
그 날에는 스터디를 진행하지 않고 이후 전체 일정을 하루 미뤄서 진행한다.
스터디를 시작하기 하루 전, 참여하는 모든 사람을 대상으로 앞으로 스터디가 예정된 K일 동안의 참석 가능 여부를 미리 조사했다. 
이 조사 결과를 보고, 스터디가 원래 예정된 날짜보다 최소 며칠이나 더 미뤄지게 될 지를 구해보자.
"""

# 입력
"""
첫째 줄에는 스터디 참여 인원 N과 스터디 진행 날짜 K가 공백을 두고 주어진다.
다음 N개의 줄에는 i번 사람의 참석 여부 a1, .. , ak가 공백을 두고 주어진다. 
aj는 i번 사람이 j일 뒤 날짜에 열리는 스터디에 참석할 수 있다면 1, 없으면 0으로 주어진다.
  • 1 ≤ N ≤ 10
  • 1 ≤ K ≤ 100
  • 0 ≤ a ≤ 1
  • 입력에서 주어지는 모든 수는 정수이다.
"""

# 입력 예시

"""
5 6
1 0 1 1 0 1
1 1 1 1 0 1
1 1 1 1 1 1
0 1 1 1 0 0
0 0 0 0 1 1
"""

# 리턴값
"""
1
"""

import sys
people, days = map(int, sys.stdin.readline().split())
data = []
for i in range(people):
    data.append(list(map(int, sys.stdin.readline().split())))

attend = []
i = 0
while i < days:
    attend.append(0)
    i += 1

answer = 0
for person in data:
    for j in range(0, days):
        if person[j] == 1:
            attend[j] += 1

for day in attend:
    if day <= people//2:
        answer += 1

print(answer)
