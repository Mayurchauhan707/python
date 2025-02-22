
my_tuple=(1,2,3,5,6,8,9,0,12,34,56,79,66,6,5,4,3,33)
new_tuple=tuple(x for x in my_tuple if x!=2 )
print(new_tuple)