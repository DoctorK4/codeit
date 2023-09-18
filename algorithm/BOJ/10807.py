import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

check_number = int(sys.stdin.readline())

answer = 0

for num in arr:
    if num == check_number:
        answer += 1

print(answer)
