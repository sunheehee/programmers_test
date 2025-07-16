def solution(n):
    numbers = range(n+1)
    array = []
    for number in numbers:
        if number % 2 ==1:
            array.append(number)
    return array