#4
x=int(input("X軸座標:"))
y=int(input("Y軸座標:"))
z=x*x+y*y
if x>0 and y>0:
    print("該點位於第一象限,離遠點距離根號",z)
elif x>0 and y<0:
    print("該點位於第二象限,離遠點距離根號",z)
elif x<0 and y>0:
    print("該點位於第四象限,離遠點距離根號",z)
elif x<0 and y<0:
    print("該點位於第三象限,離遠點距離根號",z)
elif x==0 and y==0:
    print("該點位於原點")
elif x==0 and y!=0:
    print("該點位於Y軸上,離原點距離根號",z)
elif x!=0 and y==0:
    print("該點位於X軸上,離原點距離根號",z)