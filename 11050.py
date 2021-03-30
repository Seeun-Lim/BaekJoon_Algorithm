from math import factorial
N,K=map(int,input().split())

rst=factorial(N)//(factorial(K)*factorial(N-K))
print(rst)