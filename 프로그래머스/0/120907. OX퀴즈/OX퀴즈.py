def solution(quiz):
    answer = []
    for q in quiz:
        parts = q.split()
        num1, op, num2, _, result = parts
        num1, num2, result = int(num1), int(num2), int(result)
        if op == "+":
            answer.append("O" if result == num1 + num2 else "X")
        else:
            answer.append("O" if result == num1 - num2 else "X")
    return answer
            