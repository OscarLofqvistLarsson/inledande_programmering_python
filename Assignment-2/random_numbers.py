import random

i = int(input("Enter integer u want to generate:") )

res = [random.randrange(1, 100, 1) for a in range(i) ] 

b = sum(res) / i

c = round(b, 2)

print("Generated numbers:",res)

print("Average, min and max are:",c,min(res),max(res) )