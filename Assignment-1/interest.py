s = int(input("How much do you have saved"))

p = int(input("What interest do u expect to have in procent)?"))

t = int(input("During how many years do you plan to save?"))

r = s* (p/100 + 1)**t

print(round(r), "are your savings after", t ,"years")
