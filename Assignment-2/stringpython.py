def concat(s, n):
    return s * n

def count(s, x):
    c = 0
    for i in s:
        if x == i:
                c += 1
    return c 

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

def first_last(s):
    return (s[0]),(s[-1])

def has_two_X(s): 
    i = "XX"
    if i in s:
        print("true")
    else:
        print("false")

def has_duplicates(s):
    return len([x for x in set(s) if s.count(x) > 1])