import word_set as ws
import time
import os
path = os.getcwd() + "/write_here.txt"


lista = []
with open(path, 'r', encoding='UTF-8') as file:
    for line in file:
        if len(line) > 0:
            line = line.strip('\n')
            lista.append(line)

start = time.time()
word_set = ws.new_empty_set()
for s in lista:
    ws.add(word_set,s)

#print("To_string():", ws.to_string(word_set) )  # { Owen Fred Amer Albin Måns Ola Ceve Jonas Fredrik Adam Simon Zoe David Ella Morgan }
print("Count:", ws.count(word_set))             # 15
print("Contains(Fred):", ws.contains(word_set,"fred"))   # True
print("Contains(Bob):", ws.contains(word_set,"bob"))     # False

# Hash specific data
mx = ws.max_bucket_size(word_set)
print("Max bucket:", mx)                # 2
buckets = ws.bucket_list_size(word_set) 
print("Bucket list size:", buckets)     # 20
#rint("\nCount:", ws.count(word_set))   # 11
#print("To_string():", ws.to_string(word_set) ) # { Owen Fred Amer Albin Måns Fredrik Simon Zoe David Ella Morgan }
elapsed = time.time() - start
print('Elapsed time in seconds is:',elapsed)