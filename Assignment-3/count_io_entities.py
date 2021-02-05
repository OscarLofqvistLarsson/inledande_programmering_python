import os
try:

    def hidden_dir(_dir): #function to check if subdirectories are hidden
        return _dir.name.startswith(".")

    def is_txt_file(_dir): #function to check if any text files are in subdirectories 
        return _dir.name.endswith(".txt")

    def count_directories(dir_path): 
        c_dir = 0
        _dirs = os.scandir(dir_path)
        for _dir in _dirs:
            if _dir.is_dir() and not hidden_dir(_dir) and not is_txt_file(_dir): #checking that there are any text files or hidden subdiretories
                c_dir += 1
        return c_dir        

    def count_py_files(dir_path): #counting py-files  
        c_file = 0
        f_lst = os.listdir(file_path)
        for i in f_lst:
            if i.endswith(".py"):
                c_file += 1 
        return c_file


    dir_path = os.getcwd()  #get curent working directorie 
    print(dir_path)
    print("Number of directories",count_directories(dir_path))

    file_path = "ol222hh_assign1"
    print("Number of files",count_py_files(file_path))

except IOError as e:
    print(e)
