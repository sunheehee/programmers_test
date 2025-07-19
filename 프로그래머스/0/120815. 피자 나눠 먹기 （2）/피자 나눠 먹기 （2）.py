# math모듈 활용
import math
def solution(n):
    gcd = math.gcd(6,n)
    lcm = (6 * n) / gcd
    return lcm / 6

# math 모듈 활용 x
def solution(n):
    i = 1
    while True:
        if 6 * i % n == 0:
            return i
        i += 1  
