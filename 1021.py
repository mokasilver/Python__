import collections
import sys

n, m=map(int, sys.stdin.readline().split())
targets=list(map(int, sys.stdin.readline().split()))

dq=collections.deque()

total=0

for i in range(1, n+1):
    dq.append(i)

for i in range (m):
    while True:
        if dq[0]==targets[i]:
            dq.popleft()
            break #연산 횟수 추가 X
        else:
            idx=dq.index(targets[i]) #target의 위치 찾아 idx에 저장
            if idx<=len(dq)//2:
                dq.append(dq.popleft())
            else:
                dq.appendleft(dq.pop())
            total+=1 #움직인 횟수 추가(2, 3번 연산 시)

print(total)
            
        
    
    



