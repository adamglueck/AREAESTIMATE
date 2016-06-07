from math import sin, cos, log, pi, e
num=int(input("number of pieces in piecewise function"))
totale=0
totald=0
totalf=0
totalg=0
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
    d=0
    step=(xmax-xmin)/500
    for i in range (0,500):
        i=(xmin+step/2)+step*i
        x=i
        d=d+(eval(equation2))*step
    e=0
    for i in range (0,500):
        i=(xmin+step/2)+step*i
        x=i
        e=e+(eval(equation))*step
        totald=d*(xmax-xmin)/2+totald
        totale=e+totale
    ymin=float(input("y minimum of piecewise component"))
    ymax=float(input("y maximum of piecewise component"))
    f=list(str(input("piecewise function component in terms of y ")))
    for i in range (0,len(f)):
        if f[i]=='y':
            f[i]='x'
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
    f=0
    step=(xmax-xmin)/500
    for i in range (0,500):
        i=(xmin+step/2)+step*i
        x=i
        f=f+(eval(equation2))*step
    g=0
    for i in range (0,500):
        i=(xmin+step/2)+step*i
        x=i
        g=g+(eval(equation))*step
        totalf=f*(xmax-xmin)/f+totald
        totalg=g+totalg
if num==1:
    print(d/e)
    print(f/g)
if num!=1:
    print(totald/totale)
    print(totalf/totalg)
