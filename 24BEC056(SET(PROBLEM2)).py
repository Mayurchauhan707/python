import random
def set2():
    s=set()
    while len(s)!=10:
        x=random.randint(15,45)
        s.add(x)
    print(s)
    d=set()
    c=0
    for x in s:
        if x<30:
            c=c+1
        if x>35:
            d.add(x)
            s=s-d
            print("No.of elements<30",c)
            print("after deleting all values>3")
set2()
 
