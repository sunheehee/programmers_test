def solution(numbers):
    sorted_numbers = sorted(numbers,reverse=True)
    answer = sorted_numbers[0] * sorted_numbers[1] 
    return answer