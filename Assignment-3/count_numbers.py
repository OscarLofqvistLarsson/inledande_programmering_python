try:

    def count_diffrent(lst): #counting diffrent int´s in list
        diffrent_lst = set(lst)
        return diffrent_lst

    def count_occurrences(lst): #counting how many times a int occurrs
        count = {}
        for x in lst:
            if x not in count:
                count[x] = 0
            count[x] += 1 
        return count
    
    i = [] #segment makes a list from file and enters it to function count_occurrenses(lst)
    file_a = open("file_10000integers_A.txt", "r")  
    for line_a in file_a:
        line_a = line_a.strip().split(", ")
        for k in line_a:
            i.append(int(k))
    count_a = count_occurrences(i)

    c = [] #segment makes a list from file and enters it to function count_occurrenses(lst)
    file_b = open("file_10000integers_B.txt", "r")
    for line in file_b:
        line = line.strip().split(":")
    for p in line:
        c.append(int(p))
    count_b = count_occurrences(c)

    x = 0 #segment checks the most freqvent int
    for z, v in count_a.items():
        if v > x:
            x = v
            n = z

    print("These are the diffrent integers in file_A:",count_diffrent(i))
    print("\nThe most occurring integer in file_A is:",x,"and it occurrs:",n,"times")

    x = 0 #segment checks the most freqvent int
    for z, v in count_b.items():
        if v > x:
            x = v
            n = z
    print("\nThese are the diffrent integers in file_B:",count_diffrent(c))
    print("\nThe most occurring integer in file_B is:",x,"and it occurrs:",n,"times")


except IOError as e:
    print(e)

