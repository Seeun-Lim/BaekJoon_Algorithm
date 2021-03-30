N=int(input())
stair_num=[[0]*10 for _ in range(N)]
stair_num[0]=[0,1,1,1,1,1,1,1,1,1]

for i in range(1,N):
    for j in range(10):
        if j==0:
            stair_num[i][j]=stair_num[i-1][j+1]
        elif j==9:
            stair_num[i][j]=stair_num[i-1][j-1]
        else:
            stair_num[i][j]=stair_num[i-1][j-1]+stair_num[i-1][j+1]

print(sum(stair_num[N-1])%1000000000)