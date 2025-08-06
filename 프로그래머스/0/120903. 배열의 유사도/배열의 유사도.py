def solution(s1, s2):
    result = 0
    for x in s1:
        for y in s2:
            if x == y:
                result += 1
    return result