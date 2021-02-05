print("Guess on numbers between 1- 100")

import random

count = 1

x = (random.randint(1,100))

i = int(input("Enter your number:"))

while i < x:
   print ("Too Low")
   count += 1
   
   i = int(input("Enter your number:"))

while i > x:
   print ("Too High")
   count += 1
   
   i = int(input("Enter your number:"))

if i == x:
   print ("You are Correct after",count,"tries")