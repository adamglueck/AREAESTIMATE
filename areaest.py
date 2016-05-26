from math import sin, cos, radians
f=str(input("function in terms of x using python notation"))
xmin=float(input("x min "))
xmax=float(input("x max "))
numbershapes=float(input("number of shapes "))
step=(xmax-xmin)/numbershapes
numbershapes=int(numbershapes)
a=0
for i in range (0,numbershapes):
    i=xmin+step*i
    x=i
    a=a+(eval(f))*step
a=str(a)
print("LRAM is "+a)
b=0
for i in range (1,numbershapes+1):
    i=xmin+step*i
    x=i
    b=b+(eval(f))*step
b=str(b)
print("RRAM is "+b)
c=str((float(a)+float(b))/2)
print("TRAPEZOID is "+c)
d=0
for i in range (0,numbershapes):
    i=(xmin+step/2)+step*i
    x=i
    d=d+(eval(f))*step
d=str(d)
print("MRAM is "+d)
e=str(2*(float(d)+float(c))/3)
print("SIMPSON'S is "+e)
