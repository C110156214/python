x=int(input("測試的資料量:"))
for i in range(x):
    y=input().split()
    if y[0]=="O" and y[1]=="O" :
        if y[2]=="O":
            print("YES")
        else:
            print("IMPOSSIBLE")
        continue
    elif y[0]=="O" and y[1]=="A":
        if y[2]=="A" or y[2]=="O":
            print("YES")
        else:
            print("IMPOSSIBLE")
        continue
    elif y[0]=="O" and y[1]=="B" :
        if y[2]=="B" or y[2]=="O":
            print("YES")
        else:
            print("IMPOSSIBLE")
        continue
    elif y[0]=="O" and y[1]=="AB":
        if y[2]=="A" or y[2]=="B":
            print("YES")
        else:
            print("IMPOSSIBLE")
        continue
    elif y[0]=="A" and y[1]=="A":
        if y[2]=="A" or y[2]=="O":
            print("YES")
        else:
            print("IMPOSSIBLE")
        continue
    elif y[0]=="A" and y[1]=="B":
        if y[2]=="A" or y[2]=="B" or y[2]=="O" or y[2]=="AB":
            print("YES")
        else:
            print("IMPOSSIBLE")
        continue
    elif y[0]=="A" and y[1]=="AB":
        if y[2]=="A" or y[2]=="B" or y[2]=="AB":
            print("YES")
        else:
            print("IMPOSSIBLE")
        continue
    elif y[0]=="B" and y[1]=="B":
        if y[2]=="B" or y[2]=="O":
            print("YES")
        else:
            print("IMPOSSIBLE")
        continue
    elif y[0]=="B" and y[1]=="AB":
        if y[2]=="A" or y[2]=="B" or y[2]=="AB":
            print("YES")
        else:
            print("IMPOSSIBLE")
        continue
    elif y[0]=="AB" and y[1]=="AB":
        if y[2]=="A" or y[2]=="B" or y[2]=="AB":
            print("YES")
        else:
            print("IMPOSSIBLE")
        continue
