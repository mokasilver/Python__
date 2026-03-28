#1158_요세푸스 문제

import collections
import sys

n, k=map(int, sys.stdin.readline().split())

dq=collections.deque()

final_list=[]

for i in range(1, n+1):
    dq.append(i) #dq=[1, 2, 3, 4, 5, ..., n]

for i in range(n):
            for j in range(k-1):
                dq.append(dq.popleft())
            final_list.append(dq.popleft())
      
print("<", end='')
for i in range(len(final_list)):
    print(final_list[i], end=' ')

    if i<n-1:
        print(", ", end=' ')
print(">")
        
        
