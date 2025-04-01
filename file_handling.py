#write a program to create a csv file that we can dorectly open in Ms-Excel.

f=open("C:\\Users\\24BEC056\\Desktop\\F1F2StudentsData.csv","a")
#roll no., name,CP2,maths2,physics
f.write("roll no., name, cp2,maths2,physics\n ")
rlno=input("enter the roll no.[press enter to quit]")
while rlno:
    nm=input("enter your name:")
    c,pm,p=input("enter marks of cp2,math2,physics").split(" ")
    f.write(rlno+","+nm+","+c+","+pm+","+p+"\n")
    rlno=int("enter your roll no.")
f.close()


"""
f.write("Darshit,")
f.write("shah,")
f.write("9825874525\n")
f.write("Ragi,shah,4050607080\n")
f.close()
"""
