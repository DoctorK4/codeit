def solution(emergency):
    high_priorty = sorted(emergency, reverse=True)
    answer = []
    for patient in emergency:
        found = high_priorty.index(patient) + 1
        answer.append(found)
    return answer