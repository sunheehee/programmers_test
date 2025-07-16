def solution(array):
#등장 횟수 세기
    count = {}
    for num in array:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
            
#최빈값이 2개 이상있는지 확인하기
    max_count = max(count.values())

    most_common = []
    for k,v in count.items():
        if v == max_count:
            most_common.append(k)

    #결과 도출
    if len(most_common) > 1:
        return -1
    else: 
        return most_common[0]
