
while True:
    x=input("檢測的字串(end結束):")
    if x=="end":
        break
    y=input("檢測的單一字元:")
    z=0
    x=list(x)
    for i in range(len(x)):
        if y==x[i]:
            z=z+1
    print("字元e出現次數為:",z)
    
