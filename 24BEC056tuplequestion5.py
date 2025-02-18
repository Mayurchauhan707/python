def tuple5():
    i=[(1,2),(),(3,4),()]
    print("original list =",i)
    for x in i :
        if len(x)==0:
            i.remove(x)
    print(i)
tuple5()

