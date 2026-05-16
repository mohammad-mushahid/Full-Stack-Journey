def nested():
    for i in range(1,6):
        for j in  range(1,6-i):
            print(" ",end="")
        for k in range(1,2*i):

            if i == 5  or k == 1 or  k == 2*i-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()

nested()

