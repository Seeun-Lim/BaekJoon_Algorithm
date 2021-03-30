import sys
N=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
data=sorted(data)
min_time=[0]*N

for i in range(N):
    for j in range(i+1):
        min_time[i]+=data[j]

print(sum(min_time))