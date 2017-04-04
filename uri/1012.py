line=input().split(" ")

A,B,C=line

A1=float(A)
B1=float(B)
C1=float(C)

area_react=A1*B1 #e done
area_circle=3.14159*C1*C1 #b done
area_square=B1*B1 #d done
area_trapezium= ((A1+B1)*C1/2) #c done
area_triangle= ((A1*C1)/2) #a done

print("TRIANGULO: %.3f"%area_triangle)
print("CIRCULO: %.3f"%area_circle)
print("TRAPEZIO: %.3f"%area_trapezium)
print("QUADRADO: %.3f"%area_square)
print("RETANGULO: %.3f"%area_react)
