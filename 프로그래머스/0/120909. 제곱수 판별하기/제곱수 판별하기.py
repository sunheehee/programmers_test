def solution(n):
    for i in range(1,n):
        if i ** 2 == n:
            return 1
    return 2