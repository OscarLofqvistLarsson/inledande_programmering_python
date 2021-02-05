def is_positive_and_odd(n):
    return n > 0 and n % 2 == 1

for i in range(5):
   
    n = int(input("Enter an positive and odd integer"))  
   
    if is_positive_and_odd(n):
        print("That is correct!")
        exit()

    else:
        print("Integer is either not positive or not even!")
    
print("You have tried five times!")

