#read the input
t=int(input())
# doing loop
for i in range(t):
    #read the first line
    line=input().split(' ')
    
    hour=int(line[0])
    minu=int(line[1])

    hr=["zero", "one", "two", "three", "four",
                        "five", "six", "seven", "eight", "nine",
                        "ten", "eleven", "twelve", "thirteen",
                        "fourteen","sixteen", "seventeen",
                        "eighteen", "nineteen", "twenty", "twenty one",
                        "twenty two", "twenty three", "twenty four",
                        "twenty five", "twenty six", "twenty seven",
                        "twenty eight", "twenty nine"]

    #comparing minute and print the expected value
    if minu==0:
        print("%s o' clock" %(hr[hour]))
    elif minu==1:
        print("one minute past %s" % hr[hour])
    elif minu==59:
        print("one minute to %s" % hr[(hour % 12) + 1])
    elif minu == 15:
        print("quarter past %s" %hr[hour])
 
    elif minu == 30:
        print("half past %s" %hr[hour])
 
    elif minu == 45:
        print("quarter to %s" % hr[(hour % 12) + 1])
 
    elif minu < 30:
        print("%s minutes past %s" % (hr[minu], hr[hour]))
 
    elif minu > 30:
        print("%s minutes to %s" % (hr[60 - minu], hr[(hour % 12) + 1]))
            