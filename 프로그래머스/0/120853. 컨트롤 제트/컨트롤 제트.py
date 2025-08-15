def solution (s):
    answer = 0
    prev = 0
    s = s.split()
    for ch in s:
        if ch == "Z":
            answer -= prev
        else:
            answer += int(ch)
            prev = int(ch)
    return answer