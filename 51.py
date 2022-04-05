x=list(input())
y=[]

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]==x[j]:
            y.append(x[i])
print(y)
