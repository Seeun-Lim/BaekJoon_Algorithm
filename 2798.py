N,M=map(int,input().split())
data=list(map(int,input().split()))

min_gap=M-data[0]
min_total=0
flag1=flag2=0

for i in range(N-2):
    if flag1==1:
        break
    for j in range(i+1,N-1):
        if flag2==1:
            break
        for k in range(j+1,N):
            sum=data[i]+data[j]+data[k]
            gap=M-sum
            if gap < min_gap and gap>=0:
                min_gap=gap
                min_total=sum
                if min_gap==0:
                    flag1=1
                    flag2=1
                    break
print(min_total)