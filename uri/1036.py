import math
line=input().split(' ')
a=float(line[0])
b=float(line[1])
c=float(line[2])
d=math.pow(b,2)-(4*a*c)
if(a!=0 and d>0):
    x1=(-b+(math.sqrt(d)))/(2*a)
    x2=(-b-(math.sqrt(d)))/(2*a)
    print("R1 = %.5f"%x1)
    print("R2 = %.5f"%x2)
else:
    print("%s"%"Impossivel calcular")
