n=int(input("Enter the number of rows: "))
z=n
for i in range(n):                            #loop for running number of row times

    for j in range(z):                        #loop for printing empty spaces in each row
        print(" ", end="")
    
    for l in range(2*i+1):                    #loop for printing stars in each row
        print("*", end="")   
    print("\n")
    z=z-1
