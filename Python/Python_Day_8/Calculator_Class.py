# class calculator capable of finding square, cube, square root 

class Calculator : 

    def __init__(self,n1=None,n2=None):
        self.firstNo= n1
        self.secodNo=n2
        print("Greetings!")

    def square(self):
        return pow(self.firstNo,2)
    
    def cube(self):
        return pow(self.firstNo,3)
    
    def squareRoot(self):
        return pow(self.firstNo,0.5)
    
object=Calculator(100)
print(object.firstNo)
print(object.secodNo)
square,cube,squareRoot=object.square(),object.cube(),object.squareRoot()
print(f"Square: {square}  \nCube : {cube} \nSquare Root: {squareRoot}")