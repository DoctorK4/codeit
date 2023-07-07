def solution(numbers):
    total = 0
    for item in numbers:
        total += item
    return total / len(numbers)