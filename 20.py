
x=int(input("組數為:"))
for i in range(1,x+1):
    z=0
    y=input("第{}組為:".format(i)).split()
    z=int(y[0])*250+int(y[1])*175
    print("第{}組應收費用:".format(i),z)

