T=int(input())

for _ in range(T):
    N=int(input())

    if N==0:
        print(0)
        continue

    data = dict()

    for j in range(N):
        A,B=input().split()
        if B in data.keys():
            data[B]+=1
        else:
            data[B]=1
        result=1
        for key in data.keys():
            result*=data[key]+1
    print(result-1)


