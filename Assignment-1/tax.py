income = int(input("what is your income monthly income"))


if income < 0:
    print("Invalid")

elif (income < 38000):
    print("your monthly incometax is", (income*0.30))

elif (income > 38000) and (income < 50000):
    print("your monthly income tax is", ( (38000 * 0.30) + (income - 38000) * 0.35 ) ) 

elif (income > 50000):
    print("your  monthly income tax is", ( (38000 * 0.30) + ( (50000 - 38000) * 0.35) + ((income - 50000) * 0.40) ) ) 
    