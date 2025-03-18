
"""     1
      +11
     +111
    +1111
"""
def addval(n):
  s=0
  v=n
  for i in range(4):
      s=s+n
      n=n*10+v
      print(i,n,s)
  return s

for x in range(4,8):
   print(addval(x))
