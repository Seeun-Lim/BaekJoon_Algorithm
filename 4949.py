import sys
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
    while True:
        data=input().rstrip()
        if data=='.': break

        st_small=Stack()
        st_small.clear()

        for element in data:
            if element=='(' or element=='[':
                st_small.push(element)
            elif element==')':
                if st_small.length()!=0 and st_small.beforeTop()=='(':
                    st_small.pop()
                else:
                    st_small.push(element)
            elif element==']':
                if st_small.length()!=0 and st_small.beforeTop()=='[':
                    st_small.pop()
                else:
                    st_small.push(element)
        if st_small.length()==0:
            print("yes")
        else:
            print("no")