def remov_duplicates():
    l=[ 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,0,7,55,4,,22]
    print("origional list:",l)
    l=list(set(l))
    print(l)

remov_duplicates()    