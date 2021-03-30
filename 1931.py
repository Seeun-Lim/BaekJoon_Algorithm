import sys
N=int(input())
hrs=[]
for i in range(N):
    st,end=map(int,sys.stdin.readline().split())
    hrs.append([st,end])

hrs=sorted(hrs,key=lambda x:[x[1],x[0]])
cnt=0
start=0

for i in range(N):
    if hrs[i][0]>=start:
        start=hrs[i][1]
        cnt+=1
print(cnt)
