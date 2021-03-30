T=int(input())
data=list(map(int,input().split()))
def gcd(a,b):
    r=a%b
    while r!=0:
        a=b
        b=r
        r=a%b
    return b

for i in range(1,T):
    gcd_num=gcd(data[0],data[i])
    print("%d/%d"%(data[0]//gcd_num,data[i]//gcd_num))