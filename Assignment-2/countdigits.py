number = input("Provide a positiv integer")

zero, odd, even = 0, 0, 0

for n in number:
    i = int(n)
    
    if i == 0: 
        zero = zero + 1
        
    
    elif i % 2 == 0:
        even = even + 1
        
    elif i % 2 == 1:
        odd = odd + 1
       
print("Zeros:",zero)

print("odd:",odd) 

print("Even:",even)