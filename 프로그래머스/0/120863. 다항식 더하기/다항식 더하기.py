def solution(polynomial):
    x_sum = 0  #x식
    c_sum = 0  #상수항
    for p in polynomial.split(' + '):
        if "x" in p:
            coef = p[:-1]
            x_sum += int(coef) if coef else 1
        else: 
            c_sum += int(p)
    
    result = ''
    if x_sum:
        result += "x" if x_sum == 1 else f"{x_sum}x"

    if c_sum > 0:
        if result: #x항이 이미 있다면 ' + ' 붙이기
            result += " + "
        result += str(c_sum) 
    
    return result