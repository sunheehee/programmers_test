def solution(rsp):
    answer = ''
    for result in rsp:
        if result == '2':
            answer += '0'
        elif result == '0':
            answer += '5'
        else:
            answer += '2'
    return answer