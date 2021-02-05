import os 

path_write = os.getcwd() + '\\write_here.txt'
file_test = os.getcwd() + '\\test_.txt'
file_100k = os.getcwd() + '\\eng_news_100K-sentences.txt'
file_hg = os.getcwd() + '\\holy_grail.txt'

def seperate_and_write(path):
    lines_list = []
    data = ""
    with open(path, 'r',encoding='UTF-8') as file:
        for line in file.readlines():
            for word in line:
                data += word.replace('\n',' ').strip("´“”*-'¨&#$/+»-…(•)›<>?...，|.__.—£!%;:.,\t,\n’。â€™–~‘女神為女性安全再次發聲在大會上代表運動發表消除校園暴力保障女性安全的演講（）چشماندازمذاکراتایرانوامریکابخشدومتیمآکروجتتاجطلایینیرویهواییشاهنشاهیایران").strip('"')
    data_split = data.split(" ")

    for i in data_split:
        i = i.lower()
        if i.isalpha() == True:
            lines_list.append(i+"\n")
    
    with open(path_write, 'w',encoding='UTF-8') as file_write:
        file_write.writelines(lines_list)    
    
    return lines_list    

def count_words(path):
    c = 0 
    with open(path,"r", encoding='UTF-8') as count:
        count_lines = count.readlines()
        for i in count_lines:
            if len(i) > 1:
                c += 1
    return c

def unique(path):
    st = set()
    with open(path,"r", encoding='UTF-8') as count:
        count_lines = count.readlines()
        for i in count_lines:
            st.add(i)
    return st

print(len(unique(path_write)))
seperate_and_write(file_100k)
