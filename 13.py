x=list(input("輸入字串:"))
b=list(x)
b.reverse()
y=0
a=0

for i in range(len(x)):
    if x[i]==b[i]:
        a=a+1
if a==len(x):
    print("YES")
else:
    print("NO")

