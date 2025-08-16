def solution (order):
    count = 0
    for x in str(order):
        if x in ("3","6","9"):
            count += 1
    return count
        