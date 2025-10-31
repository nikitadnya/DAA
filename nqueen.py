def issafe(board,row,col):
    for i in range(row):
     if board[i]==col or abs(board[i]-col)==abs(i-row):
        return False
    return True

def nqueen(n):
    
    board=[-1]*n
    board[0]=0
    solution=[]
    def solve(row):
     if row==n:
       solution.append(board[:])
       return
     for col in range(n):
         
         if issafe(board,row,col):
            board[row]=col
            solve(row+1)
            board[row]=-1
       
    solve(1)
    return solution

def print_board(board):
 for i in range(n):
     for j in range(n):
        print("Q" if board[i]==j else "." ,end=" ")
     print()
 print()

n=8
solution=nqueen(n)
print("Total solutions:",len(solution))
print_board(solution[0])


       



