def solution (emergency):
    sorted_emergency = sorted(emergency,reverse=True) #내림차순 정렬
    rank = {}
    for i, num in enumerate(sorted_emergency):
        rank[num] = i + 1
    result = []
    for x in emergency:
        result.append(rank[x])
    return result