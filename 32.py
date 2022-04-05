x=int(input("小明身上有幾元:"))
y=int(input("販賣機有幾種飲料:"))
a=0
for i in range(y):
    z=int(input())
    if x>=z:
        a+=1
print("小明可以買",a,"種飲料")
