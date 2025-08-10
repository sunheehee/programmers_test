def solution(num, k):
    for idx, n in enumerate(str(num), start=1):
        if int(n) == k:
            return idx
    return -1