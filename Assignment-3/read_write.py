import os
try:    
    
    lines = []
    def read_file(file_path): #segment reads file and makes it into list
    
        with open(file_path,"r") as f:
            for i in f:
                lines.append(i)
        return lines
    
    def write_file(lines, path): #makes file outoff list created in function read_file

        f = open(path,"w")
        f.writelines(lines)
        f.close()


    file_path = "mytext.txt" 

    path = r"C:\Users\osse2\OneDrive\Skola\Linnéuniversitet\Datateknik år 1\HT\Inledande programmering 1DV501\Python\python_courses\1DV501\new_text.txt"

    print(read_file(file_path) )
    write_file(lines,path)


except IOError as e:
    print(e)
