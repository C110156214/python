x=int(input("輸入一正整數:"))
if x%2==0 and x%11==0:
    if x%5!=0 and x%7!=0:
        print(x,"為新公倍數?:YES")
else:
    print(x,"為新公倍數?:NO")