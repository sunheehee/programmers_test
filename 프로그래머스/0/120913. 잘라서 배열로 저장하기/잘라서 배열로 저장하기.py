def solution(my_str, n):
    answer = []
    for i in range(0,len(my_str),n):
        chunk = my_str[i:i+n]
        answer.append(chunk)
    return answer
        