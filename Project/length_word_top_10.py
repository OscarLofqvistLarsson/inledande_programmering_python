
import table as tbl
import os
import matplotlib.pyplot as plt
import time

path = os.getcwd() + '\\write_here.txt'

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


dct = tbl.new_empty_root()
with  open(path, 'r',encoding='UTF-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        key = line
        if len(line) > 3:
            if tbl.get(dct,key) == None:
                tbl.add(dct,key,1)
            else:
                res = tbl.get(dct,key)
                tbl.add(dct,key,res+1)

all_pairs = tbl.get_all_pairs(dct)

def getkey(item):
    return item[1]
all_pairs2 = sorted(all_pairs,key=getkey,reverse=True)
print(all_pairs2[0:10])

print(f'Ord\tAntal')
for k,v in all_pairs2[0:10]:
    
    print(f'{k}\t{v}')

