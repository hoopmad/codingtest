'''
4-2. 개미와 진딧물
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ground = []
for i in range(N):
    ground.append(list(map(int, input().split())))

for y in range(-M, 0):
    print(y)
    for x in range(-M-y, M+y+1):
        print("x for: " + str(y))
