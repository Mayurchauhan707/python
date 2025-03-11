def count_lower_upper(str):
    l=0
    u=0
    for i in str :
      if(i.isupper()):
        u=u+1
      elif(i.islower()):
        l=l+1
    print("lower count :",l,"upper count:",u)




str=input("enter the string : ")
count_lower_upper(str)
