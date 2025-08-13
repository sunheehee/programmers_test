def solution(my_string, num1, num2):
    s = []
    for string in my_string:
        s.append(string)
    s[num1], s[num2] = s[num2], s[num1]
    return ''.join(s)