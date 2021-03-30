import sys
N,M=map(int,sys.stdin.readline().split())
chess=[]

def chessCheck(chess,row,col,min):
    W_index=0
    B_index=0
    for i in range(row,row+8):
        for j in range(col,col+8):
            if (i+j)%2==0:
                if chess[i][j]!='W': W_index+=1
                else: B_index+=1
            else:
                if chess[i][j]!='B': W_index+=1
                else: B_index+=1
    min.append(W_index)
    min.append(B_index)

for i in range(N):
    chess.append(list(input()))

minArr=[]

for i in range(N-7):
    for j in range(M-7):
        chessCheck(chess,i,j,minArr)
print(min(minArr))