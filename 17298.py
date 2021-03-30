n=int(input())
data=list(map(int,input().split()))
rst=[-1]*n
st=[]

st.append(0)
i=1
while st and i<n:
    while st and data[st[-1]]<data[i]:
        rst[st[-1]]=data[i]
        st.pop()
    st.append(i)
    i+=1
for i in rst:
    print(i,end=' ')