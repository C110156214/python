#10

while True:
    
        x, y = input("輸入N及M為:").split()
        if x=="0" and y=="0":
            break
        x = int(x)
        y = int(y)
        array = []
        for i in range(x):
            array.append(input("輸入矩陣數值第{}列為".format(i+1)).split())
        for i in range(y):
            for j in range(x):
                print(int(array[j][i]), end = ' ')
            print('')
    

        
