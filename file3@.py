lass matrix:
    def __init__(self, data):
        if len(data)!=3 or
any(len(row)!=3 for row in data):
            raise valueerror("matrix must be 3X3)
        self.data=data
    def display(slf):
        for rowin self.data:
            print(row)
    def add(self,other):
        result=[[self.data[i][j]=other.data[i][j] for j in range(3)]
                for i in range(3)]
        return matrix(result)
    def multiply(self,other):
        result=[[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j]+=self.data[i][k]*other.dat[k][j]
                    return matrix(result)
    def transpose(self):
        result=[[self.data[j][i] for j in range(3)]
                for i in range(
                
                        
                
