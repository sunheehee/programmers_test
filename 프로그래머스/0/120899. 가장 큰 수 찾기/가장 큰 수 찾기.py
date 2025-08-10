def solution(array):
    a = max(sorted(array))
    b = 0
    for i in range(len(array)):
        if array[i] == a:
            b = i
    answer = [a,b]
    return answer