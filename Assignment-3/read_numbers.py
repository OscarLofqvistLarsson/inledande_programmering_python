import math
try:
    def mean(lst): #function that calculate mean of given list
        mean_lst = sum(lst) / len(lst)
        return round(mean_lst,2)

    def std(lst): #function that calculate standard dervation of given list
        l = len(lst)
        m = mean(lst)
        tot_sum = 0
        for i in range(l):
            tot_sum += (lst[i] - m)**2
        return round(math.sqrt(tot_sum / l),2)

    i = [] #segment makes file into list of int´s 
    file_a = open("file_10000integers_A.txt", "r")  
    for line_a in file_a:
        line_a = line_a.strip().split(", ")
        for k in line_a:
            i.append(int(k))
    
    c = [] #segment makes file into list of int´s
    file_b = open("file_10000integers_B.txt", "r")
    for line_b in file_b:
        line_b = line_b.strip().split(":")
    for p in line_b:
        c.append(int(p))
   
    print("the mean and std for file_A is :",mean(i),std(i))
    print("the mean and std for file_B is :",mean(c),std(c))


except IOError as e:
    print(e)
