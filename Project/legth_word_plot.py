import table as tbl
import os
import matplotlib.pyplot as plt
import time

path = os.getcwd() + '\\write_here_holy_grail.txt'

#dct = {}
#with  open(path, 'r',encoding='UTF-8') as file:
   # for line in file.readlines():
   #     line = line.strip('\n')
   #     key = len(line)
  #      if key not in dct:
 #           dct[key] = 0
#        dct[key] += 1

#for k,v in sorted(dct.items()):
#    print(f'{k}\t{v}')
start = time.time()

dct = tbl.new_empty_root()
with  open(path, 'r',encoding='UTF-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        key = len(line)
        if tbl.get(dct,key) == None:
            tbl.add(dct,key,1)
        else:
            res = tbl.get(dct,key)
            tbl.add(dct,key,res+1)

lenght = []
count = []

for i in range(1,60):
    if tbl.get(dct,i) is not None:
        count.append(tbl.get(dct,i))
        lenght.append(i)


lenght_x = (lenght)
y_pos = list(range(1, len(lenght)+1))
count_y = (lenght)
print(y_pos)
plt.bar(y_pos, count)
plt.xticks(lenght)
plt.ylabel("Antal")
plt.xlabel('Ordlängd')
plt.show()

elapsed = time.time() - start
print(elapsed)