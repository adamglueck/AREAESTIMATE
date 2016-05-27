from math import sin, cos, log, tan, pi, e
function=list(str(input("function in terms of x ")))
equivs=[('ln','log'),('1x','1*x'),('2x','2*x'),('3x','3*x'),('4x','4*x'),('5x','5*x'),('6x','6*x'),('^','**'),('7x','7*x'),('8x','8*x'),('9x','9*x'),('0x','0*x'),('sec','1/cos'),('csc','1/sin'),('cot','1/tan')]
print (equivs)
for i in range (0,len(equivs)):
    searcher=list(equivs[i][0])
    searchcount=len(searcher)
    replacer=list(equivs[i][0])
    l=len(function)-searchcount+1
    for j in range (0,l):
        if function[j]==searcher[0]:
            if searchcount==1:
                print(searcher)
                print('TRUE')
            if searchcount==2:
                if function[j+1]==searcher[1] and function[j]==searcher[0]:
                    print(searcher)
                    print('TRUE')
            if searchcount==3:
                if function[j+1]==searcher[1] and function[j]==searcher[0] and function[j+2]==searcher[2]:
                    print(searcher)
                    print('TRUE')