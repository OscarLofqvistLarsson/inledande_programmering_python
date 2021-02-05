b = float(input("What is the amount of your bill?"))
print(b, "Bill")

p = float(input("How much would you like to pay?"))
print(p, "Payment")


d = p - b

if (p < b):
    print(p, "does not cover ur bill that is",b)

else:
    print(d,"Change")
    
    print(d//1000, "tusen kr")
    d = d%1000

    print(d//500, "femhundra kr")
    d = d%500

    print(d//200, "tvåhundra kr")
    d = d%200

    print(d//100, "hundra kr")
    d = d%100

    print(d//50, "femtio kr")
    d = d%50

    print(d//20, "tjugo kr")
    d = d%20

    print(d//10, "tio kr")

    print(d//5, "fem kr")
    d = d%5

    print(d//2, "två kr")
    d = d%2

    print(d//1, "en kr")
    d = d%1