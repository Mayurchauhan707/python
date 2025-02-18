def tuple4():

   pricelist=[('f1',230),('f2',300),('f3',280)]
   for x in pricelist :
    print(x)
    print(sorted(pricelist))
    import operator
    print (sorted(pricelist, key=operator.itemgetter(1),reverse=True))
tuple4()