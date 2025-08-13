def solution(numbers):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, w in enumerate(words):
        numbers= numbers.replace(w,str(i))
    return int(numbers)