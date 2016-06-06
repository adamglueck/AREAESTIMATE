from math import sin, cos, log, pi, e
num=int(input("number of pieces in piecewise function"))
area=0
b=0
area2=0
for i in range (0,num):
    xmin=float(input("x minimum of piecewise component"))
    xmax=float(input("x maximum of piecewise component"))
    f=list(str(input("piecewise function component in terms of x ")))
    for i in range (0,len(f)-1):
        if f[i]=='l' and f[i+1]=='n':
            f[i+1]='g'
            f.insert(i+1,'o')
    for i in range (0,len(f)):
        if f[i]=='^':
            f[i]='*'
            f.insert(i+1,'*')
    for i in range (0,len(f)-1):
        if f[i]=='1'and f[i+1]=='x' or f[i]=='2'and f[i+1]=='x' or f[i]=='3'and f[i+1]=='x' f[i]=='4'and f[i+1]=='x' or f[i]=='5'and f[i+1]=='x' or f[i]==6and f[i+1]=='x' or f[i]=='7'and f[i+1]=='x' or f[i]=='8'and f[i+1]=='x' or f[i]=='9'and f[i+1]=='x' or f[i]=='0' and f[i+1]=='x':
            f.insert(i+1,'*')
    for i in range (0,len(f)-2):
        if f[i]=='1' and f[i+1]=='x' or f[i]=='2' and f[i+1]=='x' or f[i]=='3' and f[i+1]=='x' f[i]=='4' and f[i+1]=='x'  or f[i]=='5' and f[i+1]=='x' or f[i]==6 and f[i+1]=='x'or f[i]=='7' and f[i+1]=='x' or f[i]=='8' and f[i+1]=='x' or f[i]=='9' and f[i+1]=='x' or f[i]=='0' and f[i+1]=='l' and f[i+2]=='n':
            f.insert(i+1,'*')
    equation=""
    for i in range (0,len(f)):
        equation=equation+f[i]
    equation2="x*("+equation+")"
    step=(xmax-xmin)/1000
    a=0
    for i in range (0,1000):
        i=xmin+step*i
        x=i
        a=a+(eval(equation2))*step
    area=area+a
    for i in range (0,1000):
        i=xmin+step*i
        x=i
        b=b+(eval(equation))*step
    area2=area2+b
print(area2/area)


