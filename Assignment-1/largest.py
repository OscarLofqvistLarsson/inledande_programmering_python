print("Provide 3 numbers")

a = int(input("Enter a:"))

b = int(input("Enter b:"))

c = int(input("Enter c:"))

if (a > b) and (a > c):
    print(a, "is the biggest number")

elif (b > a) and (b > c):
    print(b, "is the biggest number")

else:
    print(c, "is the biggest number")