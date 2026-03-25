#oops:Enapsulation

class Add:
    
    def setAdd(self, a, b):
        self.a = a
        self.b = b
        self.c = self.a + self.b
        
    def getAdd(self):
        return {"a": self.a, "b": self.b, "c": self.c}
    

obj = Add()
obj.setAdd(10, 20)
res = obj.getAdd()


print("a =", res["a"])
print("b =", res["b"])
print("add =", res["c"])


print("outside class a =", obj.a)
