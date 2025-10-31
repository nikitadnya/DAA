def fractional_knap(capacity,values,weight):
    ratio=[]
    for i in range(len(values)):
        ratio.append(values[i]/weight[i])

    index=list(range(len(values)))
    index.sort(key=lambda i : ratio[i],reverse=True)

    total_value=0
    for i in index:
        if capacity>=weight[i]:
            total_value+=values[i]
            capacity-=weight[i]
        else:
            total_value+=values[i] *(capacity/weight[i])
            break
    return total_value
values=[]
weight=[]
n=int(input("enter number of items"))
for i in range(n):
    v=int(input("Enter values of items {i+1}"))
    w=int(input("enter weights of items {i+1}"))
    values.append(v)
    weight.append(w)

capacity=int(input("enter capacity"))
result=fractional_knap(capacity,values,weight)
print("Answer is",result)



