def tuple_within_list(x):
    l=[]
    t=()
    for i in range(1,x+1):
        t=(i,i*i,i*i*i)
        l.append(t)
    return l  
   
x=int(input("Enter the ending value.:"))
print(tuple_within_list(x))                    
