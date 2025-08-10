def solution(array):
    max_val = max(array)
    for idx, val in enumerate(array):
        if val == max_val:
            return [max_val,idx]
        