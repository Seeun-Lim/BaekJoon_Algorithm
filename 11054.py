A=int(input())
data=list(map(int,input().split()))

dp=[1]*A
dp1=[1]*A

for i in range(1,A):
    for j in range(i):
        if data[j]<data[i]:
            dp[i]=max(dp[i],dp[j]+1)

for i in range(A-1,-1,-1):
    for j in range(A-1,i,-1):
        if data[j]<data[i]:
            dp1[i]=max(dp1[i],dp1[j]+1)

for i in range(A):
    dp[i]+=dp1[i]
print(max(dp)-1)


