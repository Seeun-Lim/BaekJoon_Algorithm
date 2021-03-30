import sys
T=int(input())
def findMin(x,y):
    for i in range(min(x,y),0,-1):
        if x%i==0 and y%i==0:
            break
    min_num=(x//i)*(y//i)*i
    return min_num

for i in range(T):
    A,B=map(int,sys.stdin.readline().split())
    print(findMin(A,B))

