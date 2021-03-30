import sys
class Stack(object):
    def __init__(self):
        self.stack=[]

    def push(self,num):
        self.stack.append(num)

    def pop(self):
        if self.isEmpty():
            return -1
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        if self.size()==0:
            return 1
        else:
            return 0

    def top(self):
        if self.size()==0:
            return -1
        else:
            return self.stack[self.size()-1]

if __name__=="__main__":
    N=int(input())
    st=Stack()
    for i in range(N):
        cmd_num=sys.stdin.readline().rstrip().split()
        cmd=cmd_num[0]
        if cmd=='push':
            st.push(cmd_num[1])
        elif cmd=='pop':
            print(st.pop())
        elif cmd=='size':
            print(st.size())
        elif cmd=="empty":
            print(st.isEmpty())
        else:
            print(st.top())