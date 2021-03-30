def check(num):
    arr=[]
    while num>=10:
        arr.append(num%10)
        num//=10
    arr.append(num)
    for i in range(len(arr)-2):
        if arr[i]==6 and arr[i+1]==6 and arr[i+2]==6:
            return True
            break
    return False

N=int(input())
num=665
idx=1
while idx!=N+1:
    num += 1
    if check(num):
        idx+=1

print(num)
