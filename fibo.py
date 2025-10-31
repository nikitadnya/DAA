import time
steps=0
def iterfibo(n):
    a,b=0,1
    arr=[a,b]
    global steps
    
    for i in range(n-2):
        steps+=1
        a,b=b,a+b
        arr.append(b)
    return arr
n=int(input("enter number"))
print("with iterative function",iterfibo(n))
print("number of steps",steps)

def recfibo(n):
    global recsteps
    recsteps+=1
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return recfibo(n-1)+recfibo(n-2)
    
n=int(input("enter number"))
recsteps=0 
recseq=[]  
for i in range(n):
    fibnum=recfibo(i)
    recseq.append(fibnum)
   
print("with recursive function",recseq)
print("number of steps",recsteps)   

    