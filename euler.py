startingvaluex=float(input("starting value x? "))
endingvaluex=float(input("for what x value shall I estimate y? "))
startingvaluey=float(input("starting value y? "))
step=float(input("step? "))
deriv=str(input("differential equation? "))
x=startingvaluex
y=startingvaluey

while endingvaluex>y:
  y=y+step*(eval(deriv))
  x=x+step
  print(x, y)
  
