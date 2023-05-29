import sys
from collections import defaultdict
import heapq
'''
input = sys.stdin.readline
n, m, k = map(int, input().split())

print(n, m, k)


heap = list()
print(heap)

heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 0)
print(heap)

heapq.heappop(heap)
print(heap)

heapq.heappush(heap, (-3, 3))

dic1 = defaultdict(list)
dic2 = dict()

arr = list(map(int, input().split()))

for i in arr:
    dic1[i].append(1)
    if i not in dic2.keys():
        dic2[i]=1
    else:
        dic2[i]+=1
print(dic2)
'''

is_prime = ['a' for _ in range(10)]
print(is_prime)