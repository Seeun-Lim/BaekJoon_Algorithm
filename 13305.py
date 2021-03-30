import sys
T=int(sys.stdin.readline())
distance=list(map(int,sys.stdin.readline().split()))
oil=list(map(int,sys.stdin.readline().split()))

cost=0
min=oil[0]

for i in range(T-1):
    if oil[i]<min:
        min=oil[i]
    cost+=min*distance[i]

print(cost)

