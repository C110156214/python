x=int(input())

for i in range(1,x,2):
    print((x-(x//3*2))*" ",i,end="")
    print("")
for i in range(1,x+2,2):
    print(i,end="")
for i in range(x-2,-1,-2):
    print(i,end="")
print("")
for i in range(x-2,-1,-2):
    print((x-(x//3*2))*" ",i,end="")   
    print("")