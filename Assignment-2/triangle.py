i = int(input("Enter an odd positive number"))


if i % 2 == 1 and i > 0:

    for h in range(i):
        
        for l in range(i):
        
            if(l < h):
                print(" ",end=" ")
                
            else:
                print("*",end=" ")
        print()            
    
    for h_ in range(0, i):
        
        for l_ in range(0, i - h_ - 1):
            print(end=" ")
        
        for l_ in range(0, h_ + 1):
            print("*", end=" ")
        print() 
else: 
    print("invalied number")