x=float(input("請輸入路程公里數(km):"))
a=75
if x<=1.5:
    print("所需車資為:",a)
elif x>1.5:
    if x-1.5<0.25:
        print("所需車資為:",a+5)
    elif (x-1.5)%0.25!=0:
        b=(x-1.5)//0.25+1
        a=a+b*5
        print("所需車資為:",a)
    else:
        b=(x-1.5)//0.25
        a=a+b*5
        print("所需車資為:",a)
        
