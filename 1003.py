import sys
T=int(sys.stdin.readline())

zero=[1,0,1]
one=[0,1,1]

def f(x):
    for i in range(x-2):
        zero[0]=zero[1]
        one[0]=one[1]
        zero[1]=zero[2]
        one[1]=one[2]
        zero[2]=zero[0]+zero[1]
        one[2] = one[0] + one[1]
    print(zero[2],one[2])

for i in range(T):
    zero = [1, 0, 1]
    one = [0, 1, 1]
    x=int(sys.stdin.readline())
    if x <= 2: print(zero[x], one[x])
    else:
        f(x)
