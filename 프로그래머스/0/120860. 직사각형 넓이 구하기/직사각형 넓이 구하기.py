def solution(dots):
    x_list = [dot[0] for dot in dots]
    y_list = [dot[1] for dot in dots]
    width = max(x_list) - min(x_list)
    length = max(y_list) - min(y_list)
    return width * length