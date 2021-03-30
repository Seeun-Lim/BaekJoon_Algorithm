import sys
def swap(data,i, j):
    temp = data[i]
    data[i] = data[j]
    data[j] = temp

def sort(data,start,end):
    pivot_index=end-1
    l,r=start,end-2
    pivot=data[pivot_index]

    if r-l<2: return
    while r>l:
        while data[l]<=pivot:
            l+=1

        while data[r]>=pivot:
            r-=1

        swap(pivot_index, r + 1)

    sort(0,r)
    sort(r+1,end)

N=int(input())
data=[]
for i in range(N):
    a=int(sys.stdin.readline())
    data.append(a)

sort(0,len(data))

for i in range(len(data)):
    print(data[i])