startingvaluex=float(input("starting value x? "))
startingvaluey=float(input("starting value y? "))
step=float(input("step? "))
deriv=str(input("differential equation? "))
x=startingvaluex
y=startingvaluey
while x>startingvaluex:
  y=y+step*(eval(deriv))
  x=x+step
  print(x, y)
  
