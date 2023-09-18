def solution(line):
    meets = []

    for i in range(0, len(line)-1):
        A, B, E = line[i]

        for j in range(i+1, len(line)):
            C, D, F = line[j]

            if A * D == B * C:
                continue

            x = (B * F - E * D) / (A * D - B * C)
            y = (E * C - A * F) / (A * D - B * C)

            if int(x) == x and int(y) == y:
                meets.append([int(x), int(y)])

    if len(meets) == 0:
        return None

    min_x = meets[0][0]
    max_x = meets[0][0]
    min_y = meets[0][1]
    max_y = meets[0][1]

    for i in range(0, len(meets)):
        if meets[i][0] > max_x:
            max_x = meets[i][0]
        if meets[i][0] < min_x:
            min_x = meets[i][0]
        if meets[i][1] > max_y:
            max_y = meets[i][1]
        if meets[i][1] < min_y:
            min_y = meets[i][1]

    rect_width = max_x - min_x + 1
    rect_height = max_y - min_y + 1

    rectangle = [list("." * rect_width) for i in range(rect_height)]

    for point in meets:
        dotx, doty = point
        X = dotx - min_x
        Y = rect_height - 1 - (doty-min_y)
        rectangle[Y][X] = "*"

    answer = []

    for item in rectangle:
        str = ''.join(item)
        answer.append(str)

    return answer


print(solution([[2, -1, 4], [-2, -1, 4],
      [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
