def solution(money):
    cup_count = money // 5500
    change = money - cup_count * 5500
    answer = [cup_count, change]
    return answer