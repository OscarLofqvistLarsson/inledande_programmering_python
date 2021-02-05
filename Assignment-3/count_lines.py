import os
try:
    def count_py_lines(dir_path):
        c = 0
        for sub_dir in dir_path:
            for file_dir in sub_dir:
                if file_dir.endswith(".py"):
                    for lines in file_dir:
                        c += 1
                    return c  




    dir_path = os.getcwd
    c = count_py_lines(dir_path)
    print(c)

except IOError as e:
    print(e)

#haven´t time to complete but this is my current progress    