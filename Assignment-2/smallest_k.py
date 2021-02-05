n = int(input("Enter an positive integer")) 
 
k = -1
s = 0

while s < n:
    k = k + 2
    s = s + k

print("Smallest k is", k)