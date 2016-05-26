equation=str(input("dy/dx in terms of x and y"))
xmin=int(input("left bound"))
xmax=int(input("right bound"))
ymin=int(input("lower bound"))
ymax=int(input("upper bound"))
for x in range (xmin,xmax+1):
    for y in range (ymin,ymax+1):
        print(eval(equation))
