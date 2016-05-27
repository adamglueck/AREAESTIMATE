

from math import sin, cos, log, pi, e
function=list(str(input("function in terms of x "))
equivs=[('ln','log'),('^','**'),('1x','1*x'),('2x','2*x'),('3x','3*x'),('4x','4*x'),('5x','5*x'),('6x','6*x'),('7x','7*x'),('8x','8*x'),('9x','9*x'),('0x','0*x'),('sec','1/cos'),('csc','1/sin'),('cot','1/tan')]
print equivs
"""
for i in range (0,len(f)-1):
    if f[i]=='l' and f[i+1]=='n':
        f[i+1]='g'
        f.insert(i+1,'o')
for i in range (0,len(f)):
    if f[i]=='^':
        f[i]='*'
        f.insert(i+1,'*')
for i in range (0,len(f)-1):
    if f[i]=='1' or f[i]=='2' or f[i]=='3' f[i]=='4' or f[i]=='5' or f[i]==6 or f[i]=='7' or f[i]=='8' or f[i]=='9' or f[i]=='0' and f[i+1]=='x' or f[i+1]=='l' and f[i+2]=='n':
        f.insert(i+1,'*')
equation=""
for i in range (0,len(f)):
    equation=equation+f[i]
f=equation
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
"""