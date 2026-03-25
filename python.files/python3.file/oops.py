#oops : information of class
#static parameters

class Demo:
    'this is my first python class'
    def demoData(self):
        print("Welcome to python oops")
    
print("Class Demo Info:-")
print("Class name:",Demo.__doc__)
print("Class base class:",Demo.__base__)
print("Class module :",Demo.__module__)

'''
print("Class Int Info:-")
print("Class doc string :"int.__doc__)
print("Class base name:",int.__doc__)
print("Class module:",int.__doc__)
'''
