#Display the given pyramid with step number accepted from user. 

rows = int(input("Enter the number of rows: "))  
for i in range(1, rows):  
    for j in range(1, i + 1):    
        print(i * j, end='  ')  
    print()  