# 문자열의 뒤의 n글자
# https://school.programmers.co.kr/learn/courses/30/lessons/181910

def solution(my_string, n):
    answer = ''
    answer = my_string[-n:]
    return answer