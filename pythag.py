import math #import math library

score = 0

#function returns a value (output)
def pyth(a,b):
    a = float(a)
    b = float(b)
    csquared = a*a + b*b
    c = math.sqrt(csquared) #calling the sqrt fuction from the math namespace
    return c

#function return the multiplication of two numbers
def gooble(b,x,j):
    e = b*x + 10000 - j
    return e

fooble = gooble(13,0.5,14)
print(fooble)

c = pyth(7,8)
print("Side C is " + str(c))


