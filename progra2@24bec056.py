def tuple2():
    i=[(1,'DHS',53),(3,'RDS',50),(2,'ADS',18)]
    print(i)
    rn=[]
    nm=[]
    age=[]
    for x in i:
        print(x,"\t,x[0],x[1],x[2]")
        rn.append(x[0])
        nm.append(x[1])
        age.append(x[2])
tuple2()