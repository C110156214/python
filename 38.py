x=int(input())
for i in range(x):
    y=int(input())
    if y%9==0 or y%11==0:
        print("第",i+1,"個點:",y)
        continue
    