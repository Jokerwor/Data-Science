import math
class Calculator:
    def __init__(self,square,cube,squareroot):
        self.square = square**2
        self.cube = cube**3
        self.squareroot = math.sqrt(squareroot)
c = Calculator(2,3,4)
print(c.square,c.cube,c.squareroot)
c = Calculator(4,5,6)
print(c.square,c.cube,c.squareroot)
c = Calculator(7,8,9)
print(c.square,c.cube,c.squareroot)