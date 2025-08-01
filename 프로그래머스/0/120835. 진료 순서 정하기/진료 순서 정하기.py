def solution(emergency):
    sorted_emergency = sorted(emergency,reverse=True)
    rank = {}
    i=1
    for v in sorted_emergency:
        rank[v] = i
        i += 1
    result = []
    for x in emergency:
        result.append(rank[x])
    return result