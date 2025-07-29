def solution(num_list):
    i = 1
    answer = []
    while i <= len(num_list):
        answer.append(num_list[-i])
        i += 1
    return answer
