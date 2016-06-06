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
    f2=list(str(input("piecewise function component in terms of y ")))
    for i in range (0,len(f2)-1):
        if f2[i]=='l' and f2[i+1]=='n':
            f2[i+1]='g'
            f2.insert(i+1,'o')
    for i in range (0,len(f)):
        if f2[i]=='^':
            f2[i]='*'
            f2.insert(i+1,'*')
    for i in range (0,len(f2)-1):
        if f2[i]=='1'and f2[i+1]=='x' or f2[i]=='2'and f2[i+1]=='x' or f2[i]=='3'and f2[i+1]=='x' f2[i]=='4'and f2[i+1]=='x' or f2[i]=='5'and f2[i+1]=='x' or f2[i]==6and f2[i+1]=='x' or f2[i]=='7'and f2[i+1]=='x' or f2[i]=='8'and f2[i+1]=='x' or f2[i]=='9'and f2[i+1]=='x' or f2[i]=='0' and f2[i+1]=='x':
            f2.insert(i+1,'*')
    for i in range (0,len(f2)-2):
        if f2[i]=='1' and f2[i+1]=='x' or f2[i]=='2' and f2[i+1]=='x' or f2[i]=='3' and f2[i+1]=='x' f2[i]=='4' and f2[i+1]=='x'  or f2[i]=='5' and f2[i+1]=='x' or f2[i]==6 and f2[i+1]=='x'or f2[i]=='7' and f2[i+1]=='x' or f2[i]=='8' and f2[i+1]=='x' or f2[i]=='9' and f2[i+1]=='x' or f2[i]=='0' and f2[i+1]=='l' and f22[i+2]=='n':
        f2.insert(i+1,'*')
    equation3=""
    for i in range (0,len(f2)):
        equation=equation+f2[i]
    equation4="x*("+equation+")"
    f=0
    step=(ymax-ymin)/500
    for i in range (0,500):
        i=(ymin+step/2)+step*i
        y=i
        f=f+(eval(equation2))*step
    g=0
    for i in range (0,500):
        i=(ymin+step/2)+step*i
        y=i
        g=g+(eval(equation))*step
        totalg=g*(ymax-ymin)/2+totalg
        totalf=f+totalf
if num==1:
    print(d/e)
    print(f/g)
if num!=1:
    print(totald/totale)
    print(totalf/totalg)
