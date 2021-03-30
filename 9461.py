import sys
T=int(sys.stdin.readline())
a=[0]*101
for i in range(5):
    if i<=2: a[i]=1
    else: a[i]=2

def P(x):
    for i in range(5,x+1):
        a[i]=a[i-5]+a[i-1]
    return a[x-1]

for i in range(T):
    x=int(sys.stdin.readline())
    print(P(x))