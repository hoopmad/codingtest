'''
    x만큼 간격이 있는 n개의 숫자
    https://school.programmers.co.kr/learn/courses/30/lessons/12954
'''
x = -100
n = 20

def solution(x, n):
    return [i*x + x for i in range(n)]

print(solution(x, n))