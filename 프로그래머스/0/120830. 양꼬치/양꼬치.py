def solution(n, k):
    meat = 12000 * n
    drink = 2000 * k
    discount_amount = n // 10
    answer = meat + drink - (2000 * discount_amount)
    return answer