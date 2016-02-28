#Solve me second

def solveMeSecond(a,b):
   return a+b
n = int(raw_input()) 
for _ in range(n):
    a,b = map(int,raw_input().split())
    res = solveMeSecond(a,b)
    print res