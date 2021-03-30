from math import factorial
A,K=map(int,input().split())
def cal(N,K):
    cnt=0
    while N:
        N//=K
        cnt+=N
    return cnt

print(min(cal(A,5)-cal(K,5)-cal(A-K,5),cal(A,2)-cal(K,2)-cal(A-K,2)))