#11
x,y=input("輸入月及日為:").split()
z=int(x)*100+int(y)

if z >=121 and z<=218:
    print("水瓶")
elif z>=219 and z<=320:
    print("雙魚")
elif z>=321 and z<=420:
    print("牡羊")
elif z>=421 and z<=521:
    print("金牛")
elif z>=522 and z<=621:
    print("雙子")
elif z>=622 and z<=722:
    print("巨蟹")
elif z>=723 and z<=823:
    print("獅子")
elif z>=824 and z<=923:
    print("處女")
elif z>=924 and z<=1023:
    print("天秤")
elif z>=1024 and z<=1122:
    print("天蠍")
elif z>=1123 and z<=1221:
    print("射手")
else:
    print("魔羯")
