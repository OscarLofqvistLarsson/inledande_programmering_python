n = int(input("Enter a three digit number"))

if n > 999:
    print("Too many numbers!")

else:
    a = n//100
    a = a%100
   
    b = n//10
    b = b%10

    c = n//1
    c = c%10

    print(a+b+c)