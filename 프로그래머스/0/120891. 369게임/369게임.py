def solution(order):
    answer = 0
    for x in str(order):
        if int(x) != 0 and int(x)% 3 == 0:
            answer += 1
    return answer