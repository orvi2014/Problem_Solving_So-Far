line=input().split(" ")
a,b,c,d=line
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if((b>c) and (d>a) and ((c+d)>(a+b)) and (c>0) and (d>0) and (a%2==0)):
    print("%s"%"Valores aceitos")
else:
    print("%s"%"Valores nao aceitos")
