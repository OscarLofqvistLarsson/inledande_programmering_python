s = int(input("Write time in seconds"))

h = s // 3600
s = s % 3600

m = s // 60
s = s % 60

print(h, "Hours", m, "minutes", s, "Seconds")