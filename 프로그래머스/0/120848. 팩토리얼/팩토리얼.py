def solution(n):
    answer = 0
    factorial = 1
    factorial_list = []
    i = 1
    while range(1,i+1):
        factorial *= i
        if factorial > n:
            break
        else:
            factorial_list.append(i)
            i += 1
    answer = max(factorial_list)
    return answer