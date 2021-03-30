import sys
N=int(sys.stdin.readline())
color=[]
dp=[[0]*3 for i in range(N)]

for i in range(N):
    R,G,B=map(int,sys.stdin.readline().split())
    color.append([R,G,B])

for i in range(N):
    if i==0:
        dp[i]=color[i]
    else:
        dp[i][0]=color[i][0]+min(dp[i-1][1],dp[i-1][2])
        dp[i][1] = color[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = color[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(min(dp[N-1][0],dp[N-1][1]),dp[N-1][2]))
