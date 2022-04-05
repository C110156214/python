while True:
    x=input("輸入整數數列(end結束):")
    if x=="end":
        break
    x=list(x)
    b=list(x)
    b.reverse()
    y=0
    a=0
    for i in range(len(x)):
        if x[i]==b[i]:
            a=a+1
    if a==len(x):
        print("YES")
    else:
        print("NO")





