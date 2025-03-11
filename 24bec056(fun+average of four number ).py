def avg(a,b,c,d):
    sum=(a+b+c+d)
    average=(a+b+c+d)/4
    return average,sum
    



a=int(input("enter the num1:"))
b=int(input("enter the num2:"))
c=int(input("enter the num3:"))
d=int(input("enter the num4:"))
sum,average=avg(a,b,c,d)

print("the average is :",average, "the sum is :",sum)

