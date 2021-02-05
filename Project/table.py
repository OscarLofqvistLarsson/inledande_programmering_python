# A binary search based dictionary imlementation 
# only using list of length 4.

# Each node is a list of length four where positions
# 0 = key, 1 = value, 2 = left-child, 3 = right-child


# Creates and returns the root to a new empty table.
# The complete function is given and should not be changed.
def new_empty_root():
    return [None,None,None,None]

# Add a new key-value pair to table if the key doesn't already exist.
# Update value if already key exists in the table.
def add(root,key,value):
    if root[0] is None: #check if root[0] is empty, if if is, adds key and value to root[0] and root[1]
        root[0] = key
        root[1] = value
    else:
        if root[0] > key: # If the key is smaller than root[0], go left
            if root[2] == None:
                root[2] = [key,value,None,None]
            else:
                add(root[2],key,value)
        elif root[0] < key: #If the key is larger than root[0], go right
            if root[3] == None:
                root[3] = [key,value,None,None]
            else:
                add(root[3],key,value)
        else:
            root[0] = key
            root[1] = value




# Returns a string representation of the table content.
# That is, all key-value pairs
def to_string(node):
    r = '{ '
    r += rec(node)
    r += '}'
    return r

def rec(node):
    string = ''
    if node[0] is not None:
        if node[2] is not None:
            string += rec(node[2])
        string += '(' + node[0] + ',' + str(node[1]) + ') '
        if node[3] is not None:
            string += rec(node[3])
    return string

# Returns the value for the given key. Returns None if key doesn't exists.
def get(node,key):
    if node[0] is None:
        return None
    if node[0] == key: #if node 0 is the key, return value
        return node[1]
    else:
        if node[0] > key: # Check if the key is smaller than the key in node 0, if true, go left
            if node[2] is None: # If node[2] is empty, key doesn't exist
                return None
            else:
                return get(node[2],key)
        elif node[0] < key: #Check if the key is larger then the key in node 0, if true go right
            if node[3] is None: # If node[3] is empty, key doesn't exist
                return None
            else:
                return get(node[3],key)

# Returns the maximum depth (an integer) of the tree.
# That is, the length of longest root-to-leaf path.

def max_depth(node): # modified code from https://stackoverflow.com/questions/45982591/maximum-depth-of-a-binary-tree-in-python
    count = 1
    if node is None:
        return count - 1
    else:
        left = 1 + max_depth(node[2])
        right = 1 + max_depth(node[3])
        return max(left,right)

# Returns the number of key-value pairs currently stored in the table

def count(node):
    c = 0
    if node[0] is not None:
        c+=1
        if node[2] is not None:
            c += count(node[2])
        if node[3] is not None:
            c += count(node[3])
    return c

# Returns a list of all key-value pairs as tuples 
# sorted as left-to-right, in-order
def get_all_pairs_rec(root,lst):
    if root[0] is not None:
        tup = (root[0],root[1])
        if root[2] is not None:
            get_all_pairs_rec(root[2],lst)
        lst.append(tup)
        if root[3] is not None:
            get_all_pairs_rec(root[3],lst)
    return lst

def get_all_pairs(root):
   lista = []
   get_all_pairs_rec(root,lista)
   return lista 