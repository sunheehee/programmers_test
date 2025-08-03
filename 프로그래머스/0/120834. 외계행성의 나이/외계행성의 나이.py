def solution(age):
    alpha = ['a','b','c','d','e','f','g','h','i','j']
    age = str(age)
    answer = ''
    for a in age:
        answer += alpha[int(a)] 
    return answer