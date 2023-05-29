'''
4-1. 제곱암호
'''

import sys
input = sys.stdin.readline

n = int(input())
s = list(input().rstrip())
msg = ''

for i in range(0, n, 2):
    c = s[i]
    num = int(s[i+1])
    # ascii값을 활용해 a부터 z까지의 값이 되도록 계산
    de = chr((ord(c)-ord('a') + num*num) % 26 + ord('a'))
    msg += de

print(msg)