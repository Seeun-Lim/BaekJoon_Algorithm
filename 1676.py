from math import factorial
T=int(input())
FT=factorial(T)

cnt=0
while True:
    if FT%10!=0:break
    FT//=10
    cnt+=1
print(cnt)
    