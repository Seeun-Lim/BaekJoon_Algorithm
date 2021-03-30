def newNum(a):
    nN=a
    while a>=10:
        nN+=(a%10)
        a//=10
    nN+=a
    return nN

N=int(input())
i=1
while True:
    if i>=N:
        a=0
        break
    if newNum(i+1)==N:
        a=i+1
        break
    i+=1

print(a)