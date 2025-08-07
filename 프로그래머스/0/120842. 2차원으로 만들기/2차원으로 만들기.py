def solution(num_list, n):
    answer = []
    for i in range (0, len(num_list)-1, n):
        a = num_list[i:i+n]
        answer.append(a)
    return answer