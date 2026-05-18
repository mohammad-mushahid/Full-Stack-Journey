def nested():
 i = 1
 num = int(input("Enter the number: "))
 while i<= num:
     if i % 2 == 0:
         print("even")
     if i % 2!= 0:
        print("odd")
     i += 1
nested()
