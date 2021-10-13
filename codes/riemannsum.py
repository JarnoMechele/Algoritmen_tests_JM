# riemannSum on the function f(x) = x^2

def riemannSum(x,y,n):
  fx = 0
  divisions = (y - x)/n
  for i in range(1,n):
    fx += ((x+(i * divisions))**2)
    fx += y **2
  
  return divisions * fx

print (riemannSum(2,3,4))
