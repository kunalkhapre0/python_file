#oops:data member & member method

class Add:
    a, b, c = 0, 0, 0

    def getData(self):
        self.a = 100
        self.b = 200

    
    def addData(self):
        self.c = self.a + self.b

   
    def showData(self):
        print("a =", self.a)
        print("b =", self.b)
        print("add =", self.c)

obj = Add()
obj.addData()    
obj.showData()   
