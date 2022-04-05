a=[]
b=[]
a.append(input("sA:"))
b.append(input("sB:").split())

if a[0] in b[0]:
    print("子字串判斷為:YES")
else:
    print("子字串判斷為:NO")

    
print(a,b)