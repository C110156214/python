x=list(input("假設答案為:"))
while True:
    y=input()
    if y=="0000":
        break
    y=list(y)
    a=0
    b=0
    for i in range(4):
        if y[i]== x[i]:
           a=a+1
        elif y[i]in x:
            b=b+1
    print(a,"A",b,"B")
        

