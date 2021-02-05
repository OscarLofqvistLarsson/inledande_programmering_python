import random

res = []
dice1 = [random.randrange(1, 7, 1) for a in range(10000) ]
dice2 = [random.randrange(1, 7, 1) for a in range(10000) ]

for i in range(len(dice1) ):
    res.append(dice1[i] + dice2[i])

n2 = res.count(2)
n3 = res.count(3)
n4 = res.count(4)
n5 = res.count(5)
n6 = res.count(6)
n7 = res.count(7)
n8 = res.count(8)
n9 = res.count(9)
n10 = res.count(10)
n11 = res.count(11)
n12 = res.count(12)

print("2:"            ,n2)
print("3:"            ,n3)
print("4:"            ,n4)
print("5:"            ,n5)
print("6:"            ,n6)
print("7:"            ,n7)
print("8:"            ,n8)
print("9:"            ,n9)
print("10:"           ,n10)
print("11:"           ,n11)
print("12:"           ,n12)