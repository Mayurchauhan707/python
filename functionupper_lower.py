def count_lower_upper(str):
    
    l=0
    u=0
    for i in str :
      if  i>='a'and i<='z':
        l=l+1
      elif i>='A'and i<='Z':
        u=u+1
    print("lower count :",l,"upper count:",u)
"""  for i in str :
      if(i.isupper()):
        u=u+1
      elif(i.islower()):
l=l+1"""
    

str=input("enter the string : ")
count_lower_upper(str)
