N=int(input())
data=[]
size=[]

for i in range(N):
    x,y=map(int,input().split())
    data.append([x,y])
    size.append(1)

for i in range(N):
    for j in range(N):
        if data[i][0]<data[j][0] and data[i][1]<data[j][1]:
            size[i]+=1

for i in size:
    print(i,end=' ')
