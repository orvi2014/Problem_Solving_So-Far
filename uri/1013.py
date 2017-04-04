line=input().split(" ")
a = int(line[0]);
b = int(line[1]);
c = int(line[2]);

maiorAB = ((a + b) + abs(a-b))/2;
maiorAC = ((a + c) + abs(a-c))/2;
maior = ((maiorAB + maiorAC) + abs(maiorAB-maiorAC))/2;

print("%d eh o maior" % maior);
