num=int(input())
hour=int(num/3600)
minu_extra= num%3600
minu=int(minu_extra/60)
sec=int(num%60)

print("%d:%d:%d"%(hour,minu,sec))
