import sys
from collections import deque

T=int(sys.stdin.readline())
Queue=deque([])

for i in range(1,T+1):
    Queue.append(i)

while True:
    if len(Queue)==1: break
    Queue.popleft()
    data=Queue.popleft()
    Queue.append(data)
print(Queue[0])

