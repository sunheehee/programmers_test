def solution(my_string):
    string = my_string.split()
    result = int(string[0])
    
    for i in range (1, len(string), 2):
        operator = string[i]
        number = int(string[i+1])
        if operator == "+":
            result += number
        if operator == "-":
            result -= number
    return result