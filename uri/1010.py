line1 = input().split(" ")
line2 = input().split(" ")

cod1, q1, v1 = line1
cod2, q2, v2 = line2

total = (int(q1) * float(v1)) + (int(q2) * float(v2))

print("VALOR A PAGAR: R$ %0.2f" %total)
