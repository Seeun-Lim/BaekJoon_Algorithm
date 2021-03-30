import sys
N,K=map(int,sys.stdin.readline().split())
coin=[]
result=0
for i in range(N):
    coin.append(int(sys.stdin.readline()))

for i in range(N-1,-1,-1):
    result+=(K//coin[i])
    K%=coin[i]
    if K==0: break
print(result)