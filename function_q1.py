#print 1st n natural nos using recursion.
"""def natural(n):
    if n==0:
        return
    else:
        print(n)
        natural(n-1)
natural(5)
 """
"""def natural(n):
    if n==6:
        return
    else:
        print(n)
        natural(n+1)
natural(1)

def natural(n):
    if n==0:
        return
    else:
        natural(n-1)
        print(2*n+1)
       
natural(5)
 

def print_word():
    print("welcome")
def add(a,b,c):
    c()
    print(a+b)
def minus(a,b,c):
    c()
    print(a-b)
f=print_word
add(5,10,f)
minus(10,5,f)"""
"""
r=lambda n:n**2
print("result")
print(r(3))
print(r(5))"""
"""
r=lambda n,p,q:n+p+q
print("result")
print(r(3,4,5))
print(r(5,10,15))
"""
"""
list1=[1,2,3,4,5,6,7,8,9,10]
even=[]
even=filter(lambda n:n%2==0 ,list1)
print(list(even))

"""
"""
list1=[1,2,3,4,5,6,7,8,9,10]
even=[]
even=filter(lambda n:n%2!=0 ,list1)
print(list(even))

"""
def sum(a,b):
  return a+b
from function import reducef                                                          
list1=[1,3,5,8,10,20]
r=reduce(sum,list1)
print(r)




































