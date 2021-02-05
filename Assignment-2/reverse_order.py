print("Enter positive integer. End with a negative integer.")

nr = []
c = 0
n = int(input("Enter integer") )

while n > 0:
    c += 1 
    print()
    nr.append(n)
    
    n = int(input("Enter integer") )
    
    if n < 0: 
        break    

for i in range(0, n):
    nr.append(n)
    
nr.reverse()

print("Positive integers:",c)
print("in reverse order:",nr)