class Stack():
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if len(self.stack)==0:
            return -1
        return self.stack.pop()
    def clear(self):
        self.stack=[]
    def printStack(self):
        for i in self.stack:
            print(i,end=' ')
        print()
    def length(self):
        return len(self.stack)
    def beforeTop(self):
        return self.stack[len(self.stack)-1]

if __name__=="__main__":
    T=int(input())
    for i in range(T):
        data=input()
        st=Stack()
        st.clear()
        for element in data:
            if element=='(':
                st.push(element)
            else:
                if st.length()!=0 and st.beforeTop()=='(':
                    st.pop()
                else:
                    st.push(element)

        if st.length()==0:
            print("YES")
        else:
            print("NO")