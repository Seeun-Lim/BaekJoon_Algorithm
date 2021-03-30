import sys
from collections import deque

T=int(sys.stdin.readline())
Queue=deque([])

for i in range(T):
    cmd_num = sys.stdin.readline().rstrip().split()
    cmd = cmd_num[0]

    if cmd=='push':
        data = int(cmd_num[1])
        Queue.append(data)
    elif cmd=='front':
        if Queue:
            print(Queue[0])
        else:
            print("-1")
    elif cmd == 'back':
        if Queue:
            print(Queue[len(Queue)-1])
        else:
            print("-1")
    elif cmd == 'pop':
        if Queue:
            print(Queue.popleft())
        else:
            print("-1")
    elif cmd == 'size':
        print(len(Queue))
    elif cmd == 'empty':
        if Queue:
            print("0")
        else:
            print("1")