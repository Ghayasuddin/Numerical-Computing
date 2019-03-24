import math

def fun(p):
  #return math.sin(p)
  #return math.exp(p) + math.sin(2 * p)
  return (p * p * p * p) - (p * p) - 2

a=0
b=0

print("Enter Value of a: ")
a = float(input())

print("Enter Value of b: ")
b = float(input())

print("i\t\ta\t\tb\t\tf(a)\t\tf(b)\t\tc\t\tf(c)\n")
pre = 1
d = 0
i=0

while (abs(pre-d)) > 0.001:
  if i != 0:
    pre = d
  c = (a+b)/2
  y = fun(a)
  z = fun(b)
  d = fun(c)

  print(i+1,"\t","%.4f"%a, "\t  ", "%.4f"%b,"\t ","%.4f"%y ,"\t","%.4f"%z,"\t", "%.4f"%c, "\t  %.4f"%d,"\n")
  
  if d > 0:
    b = c
  else:
    a = c
  i = i + 1

  