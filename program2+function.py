"""
create a array() and return in 3D ARRAY
"""
"""def create_array1(x,n):
    I=[]
    for i in range(x):
        I=I+[n]
    return I
x=int(input("how many element you want to create in an array:"))
n=int(input("with what value should i initialize this array:"))
a1=create_array1(x,y,n)
print(a1)"""

"""def create_array1(  x,y,n):
    I=[]
    for i in range(x):
        for J in range(y):
           I=I+[n]
    
    return I
x=int(input("how many rows do you want to create in an array:"))
y=int(input("how many rows do you want to create in an array:"))
n=int(input("with what value should i initialize this array:"))
a2=create_array1(x,y,n)
print(a2)
"""
def create_array3(x, y, z, n):
    l = []
    for i in range(x):
        m = []
        for j in range(y):
            row = [n] * z  # Create a list of length z initialized with n
            m.append(row)  # Append the row to the matrix
        l.append(m)  # Append the 2D matrix to the 3D array
    return l

# Taking user input for dimensions and initialization value
x = int(input("How many rows do you want in array: "))
y = int(input("How many columns do you want in array: "))
z = int(input("How many elements do you want in z: "))
n = int(input("With what value should I initialize this array: "))

# Creating and printing the 3D array
a3 = create_array3(x, y, z, n)
print(a3)
