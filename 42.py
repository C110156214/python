x=int(input())
y=int(input())
z=int(input())
q=y**2-4*x*z

if q>0:
    print(((y*-1)+(q**0.5))/(2*x),((y*-1)-(q**0.5))/(2*x))
elif q==0:
    print((-1*y)/(2*x))
else:
    print("無解")