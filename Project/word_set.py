# A list based hash table implementation for strings.
# Initial bucket size is 10, we the double the bucket size
# when nElements = bucketSize.
#if w not in bucket. bucket.append(w)
size = 0      # global variable, current number of elements

# Returns a new empty set
# The complete function is given and should not be changed.
def new_empty_set():
    global size
    size = 0
    buckets = []
    for i in range(10):
        buckets.append([])
    return buckets

def hash_word(word_set, word):
    key = 0
    for i in word:
        key += ord(i)
    key %= len(word_set)
    return key

# Adds word to word set if not already added
def add(word_set, word):
    global size
    key = hash_word(word_set, word)
    if word not in word_set[key]:
        word_set[key].append(word)
        size += 1
    if size == len(word_set):
        return rehash(word_set)
    
# Returns current number of elements in set
def count(word_set):
    return size

# Returns current size of bucket list
def bucket_list_size(word_set):
    return len(word_set)


# Returns a string representation of the set content
def to_string(word_set):
    allt = '{ '
    for i in word_set:
        for b in i:
            allt += b + ' '
    allt += '}'
    return allt

# Returns True if word in set, otherwise False    
def contains(word_set, word):
    key = hash_word(word_set, word)
    for i in word_set[key]:
        if i == word:
            return True
    return False

# Removes word from set if there, does nothing 
# if word not in set
def remove(word_set, word):
    global size
    key = hash_word(word_set, word)
    for i in word_set[key]:
        if i == word:
            word_set[key].remove(word)
            size -= 1

# Returns the size of the bucket with most elements
def max_bucket_size(word_set):
    count_max = 0
    count = 0
    for i in word_set:
        count = len(i)
        if count > count_max:
            count_max = count
    return count_max

# rehashes the list to duouble size
def rehash(word_set):
    old = []
    global size
    len_ = len(word_set)
    for bucket in word_set:
        for items in bucket:
            old.append(items)
    word_set.clear()
    for i in range(len_*2):
        word_set.append([])
    size = 0
    for v in old:
        add(word_set,v)