class number:
    def __init__(self,n=0):
        self.num=n
        #print(self)

    def isodd(s):
        #print(s)
        return True if s.num%2!=0 else False

    def isperfect(t):
        s=0
        for d in range(1,t.num//2+1):
            if t.num%d==0:
                s=s+d
        return True if t.num==s else False

a=number(31)
print(a.isperfect())
print(a.isodd())
