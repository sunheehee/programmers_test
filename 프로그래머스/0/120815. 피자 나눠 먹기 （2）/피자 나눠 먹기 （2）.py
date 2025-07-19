import math
def solution(n):
    gcd = math.gcd(6,n)
    lcm = (6 * n) / gcd
    return lcm / 6