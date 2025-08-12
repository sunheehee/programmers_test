def solution(array, n):
    diff_list = []
    for num in array:
        diff_list.append(abs(num-n))
    
    min_diff = min(diff_list)
    answer = []
    for i, diff in enumerate(diff_list):
        if diff == min_diff:
            answer.append(array[i])
    return min(answer)