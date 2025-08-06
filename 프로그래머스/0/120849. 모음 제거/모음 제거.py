def solution(my_string):
    answer = ''
    vowel=['a','e','i','o','u']
    for v in vowel:
        my_string = my_string.replace(v,'')
    return my_string