N=int(input())
wine=[int(input()) for x in range(N)]

dp=[0]
dp.append(wine[0])
if N>1: dp.append(wine[0]+wine[1])

for i in range(3,N+1):
    dp.append(max(wine[i-1]+dp[i-2],wine[i-1]+wine[i-2]+dp[i-3],dp[i-1]))

print(dp[N])
