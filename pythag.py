import math #import math library
#function returns a value (output)
def pyth(a,b):
    a = float(a)
    b = float(b)
    csquared = a*a + b*b
    c = math.sqrt(csquared) #calling the sqrt fuction from the math namespace
    return c
    
c = pyth(4,7)
print("Side C is " + str(c))
c = pyth(5.6,7.8)
print("Side C is " + str(c))
c = pyth(6,9)
print("Side C is " + str(c))