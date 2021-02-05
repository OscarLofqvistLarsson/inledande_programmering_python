c = 0

for i in range(100,201):
    
    if i % 4 == 0 and not i % 5 == 0:
        
        print(i, end=" ")
       
        c += 1
        
        if c % 10 == 0:
            print()
            

    elif i % 5 == 0 and not i % 4 == 0:
        
        print(i, end=" ")
        
        c += 1
        
        if c % 10 == 0:       
            print()
            