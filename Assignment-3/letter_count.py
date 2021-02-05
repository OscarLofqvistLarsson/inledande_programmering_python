try:

    file_holy_grail = open("holy_grail.txt", "r", errors = "ignore")

    charcount = {} 
    validchars = "abcdefghijklmnopqrstuvwxyz" #char that i want to count 

    for i in range(97,123): #97-123 is assci numbers for lowercase a-z
        c = (chr(i)) 
        charcount[c] = 0 
 
    for line in file_holy_grail: #segment count letters in file 
        words = line.split(" ") 
        for word in words:  
            chars = list(word) 
        for c in chars:  
            if c.isalpha(): 
                if c.isupper():
                    c = c.lower()  
                if c in validchars: 
                    charcount[c] += 1 

    print("reading text from file holy_grail.txt")
    sum_ = 0 #segment sum all letters in file           
    for i in charcount.values():
        sum_ = sum_ + i

    print("total number of letters in holy_grail.txt:",sum_)
    print("Histogram where each star represent 200 occurences")

    for k, v in charcount.items(): 
        print(f"{k} | {(v//200) * '*'}") #makes my value v to be represented in stars

 
    file_100k = open("eng_news_100k-sentences.txt", "r", errors = "ignore")

    charcount = {} 
    validchars = "abcdefghijklmnopqrstuvwxyz" #char that i want to count 

    for i in range(97,123): #97-123 is assci numbers for lowercase a-z
        c = (chr(i)) 
        charcount[c] = 0 
 
    for line in file_100k: #segment count letters in file
        words = line.split(" ")
        for word in words:  
            chars = list(word) 
        for c in chars:  
            if c.isalpha(): 
                if c.isupper():
                    c = c.lower()  
                if c in validchars: 
                    charcount[c] += 1 

    print("Reading text from file eng_news_100k-senteces.txt")

    sum_ = 0 #segment sum all letters in file             
    for i in charcount.values():
        sum_ = sum_ + i
    print("total numbers of letters in eng_news_100k-sentences.txt:",sum_)

    print("Histogram where each star represent 10000 occurences")
    for k, v in charcount.items(): #makes my value v to be represented in stars
        print(f"{k} | {(v//10000) * '*'}")
            

except IOError as e:
    print(e)
