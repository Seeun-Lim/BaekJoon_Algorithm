class Stack():
    def __init__(self):
        self.stack=[]
    def push(self,num):
        self.stack.append(num)
    def pop(self):
        return self.stack.pop()
    def size(self):
        return len(self.stack)
    def get(self,idx):
        return self.stack[idx]

if __name__=="__main__":
    K=int(input())
    st=Stack()
    sum=0

    for i in range(K):
        n=int(input())
        if n==0:
            st.pop()
        else:
            st.push(n)

    for i in range(st.size()):
        sum+=(st.get(i))
    print(sum)