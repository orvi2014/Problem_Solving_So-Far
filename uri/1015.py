import math
line1=input().split(" ")
line2=input().split(" ")
x1=float(line1[0])
x2=float(line2[0])
y1=float(line1[1])
y2=float(line2[1])
dis=math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))
print("%.4f"%dis)
