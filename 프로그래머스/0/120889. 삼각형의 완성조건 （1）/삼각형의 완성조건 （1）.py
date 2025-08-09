def solution(sides):
    sides = sorted(sides)
    if sides[-1] < sum(sides[0:-1]):
        return 1
    return 2