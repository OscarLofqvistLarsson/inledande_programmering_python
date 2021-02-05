import random

def random_list(n):
    lst =[random.randrange(1,101) for i in range(n)]
    return lst

def function_average(lst):
    res = sum(lst)
    i = len(lst)
    avg = res / i
    
    return round(avg)

def only_odd(lst):
    odd = [num for num in lst if num % 2 == 1]
    return odd

def to_string(lst):
   
    return str(lst), type(str(lst))

def contains(lst, a, b):
    con = False
    
    for a in lst:
        if a + 1 == b: 
           con = True
    return con

def has_duplicates(lst):
    return len([n for n in set(lst) if lst.count(n) > 1])
