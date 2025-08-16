def solution(my_string):
    total = 0
    curr = ''
    
    for string in my_string:
        if string.isdigit():
            curr += string
        else:
            if curr:
                total += int(curr)
                curr = ''
    if curr:
        total += int(curr)
    return total