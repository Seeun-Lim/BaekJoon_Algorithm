import sys
def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

def selectionSort(data):
    for i in range(len(data)-1):
        pivot=min=data[i]
        min_index=i
        for j in range(i+1,len(data)):
            if data[j]<min:
                min=data[j]
                min_index=j
        swap(data,i,min_index)

    for i in data:
        print(i)

if __name__=="__main__":
    N=int(sys.stdin.readline())
    data=[]
    for i in range(N):
        a=int(sys.stdin.readline())
        data.append(a)
    selectionSort(data)
