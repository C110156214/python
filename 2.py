#2
x=int(input("請輸入度數(正整數):"))

if 0<x<121:
    print("夏月:",(x*2.1)," 非夏月:",x*2.1)
elif 120<x<331:
    print("夏月:",120*2.1+(x-120)*3.02," 非夏月:",120*2.1+(x-120)*2.68)
elif 330<x<501:
    print("夏月:",120*2.1+210*3.02+(x-330)*4.39," 非夏月:",120*2.1+210*3.02+(x-330)*3.61)
elif 500<x<701:
    print("夏月:",120*2.1+210*3.02+170*4.39+(x-500)*4.97," 非夏月:",120*2.1+210*3.02+170*4.39+(x-500)*4.01)
else:
    print("夏月:",120*2.1+210*3.02+170*4.39+200*4.97+(x-700)*5.63," 非夏月:",120*2.1+210*3.02+170*4.39+200*4.97+(x-700)*4.5)
