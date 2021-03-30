import sys
def gcd(a,b):
    r=a%b
    while r!=0:
        a=b
        b=r
        r=a%b
    return b

T=int(sys.stdin.readline())
data=[]
for i in range(T):
    data.append(int(sys.stdin.readline().rstrip()))
data.sort()
gcd_num=data[1]-data[0]

for i in range(2,T):
    gcd_num=gcd(gcd_num,data[i]-data[i-1])
M=[gcd_num]
for i in range(2,int(gcd_num**0.5)+1):
    if gcd_num%i==0:
        print(i,end=' ')
        if i!=gcd_num//i:
            M.insert(0,gcd_num//i)
for i in M:
    print(i,end=' ')