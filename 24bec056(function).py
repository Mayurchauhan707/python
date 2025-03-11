"""def add():
    n1=int(input("enter the number: "))
    n2=int(input("enter the second number :"))
    s=n1+n2
    print("addition of two number is :",s)
add()"""
def add(n1,n2):
    s=n1+n2
    print("addition of two number is :",s)
def sub(n1,n2):
    s=n1-n2
    print("substraction of two number is :",s)
def multiply(n1,n2):
    s=n1*n2
    print("multiplication of two number is :",s)
def div(n1,n2):
    s=n1/n2
    print("division of two number is :",s)

n1=int(input("enter the number:"))
n2=int(input("enter the second number :"))
oprator=input("enter the oprator:+,-,/,* :")
if oprator=='+':
    add(n1,n2)
elif oprator=='-':
    sub(n1,n2)
elif oprator=='*':
    multiply(n1,n2)
elif oprator=='/':
    div(n1,n2)

