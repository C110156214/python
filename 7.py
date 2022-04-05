#7
x,y=input("輸入月租費型式及通話時間為:").split(",")
z=0
if x=="186":
    if int(y)<=186:
        z=int(y)*0.09*0.9
    else:
        z=int(y)*0.09*0.8
elif x=="386":
    if int(y)<=386:
        z=int(y)*0.08*0.8
    else:
        z=int(y)*0.08*0.7
    

print("{:.2f}".format(z))