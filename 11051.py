from math import factorial
import sys
T=int(input())
def cal(N,K):
    rst = factorial(N) // (factorial(K) * factorial(N - K))
    return rst

for i in range(T):
    N,K=map(int,sys.stdin.readline().split())
    print(cal(K,N))