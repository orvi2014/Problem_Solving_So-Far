num=float(input())
if(num>=0 and num<=100):
    if(num>=0 and num <=25):
        print("%s"%"Intervalo [0,25]")
    else:
        if(num>25 and num<=50):
            print("%s"%"Intervalo (25,50]")
        else:
            if(num>50 and num<=75):
                print("%s"%"Intervalo (50,75]")
            else:
                print("%s"%"Intervalo (75,100]")
else:
    print("%s"%"Fora de intervalo")
