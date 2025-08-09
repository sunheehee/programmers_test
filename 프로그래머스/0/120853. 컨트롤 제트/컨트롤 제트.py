def solution(s):
    list = []
    s = s.split()
    for ch in s:
        if ch == 'Z':
            list.pop()
        else:
            list.append(int(ch))
    return sum(list)