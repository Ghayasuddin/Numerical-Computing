import math
import array as arr
    
def fun(p):
    #return math.sin(p)
    #return math.exp(p) + math.sin(2 * p)
    return (p * p * p * p) - (p * p) - 2

def der(p):
    #return math.cos(p)
    #return math.exp(p) + 2 * math.cos(2 * p)
    return (4 * p * p * p) - (2 * p * p)

print("Enter Value of x: ")
x = float(input())

print("iteration \t\t\t x0 \t\t\t  f(x) \t\t\t\t f'(x) \t\t\t\t x1 \n")
c = -1.1

i=0
while (abs(x-c) > 0.0001) or (i>30):
    if i != 0:
        x = c
    a = fun(x)
    b = der(x)
    c = x - (a/b)
    print(i+1, "\t\t\t", "%.4f" % x , "\t\t\t", "%.4f" % a, "\t\t\t", "%.4f" % b, "\t\t\t", "%.4f" % c, "\n")
    i = i + 1

if i >= 30:
    print("The Answer was not found after 30 iteration")
else:
    print("The Real Root of  f(x) is ", "%.4f" % c)