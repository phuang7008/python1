import os
#from path import Path

# get input file name from user
file_name = input("Please enter the file name: ")
if len (file_name) < 1:
    file_name = os.path.normpath(r"C:/Users/ting/Downloads/Ccode_dump.txt")
    file_name =("C:\\Users\\ting\\Downloads\\Ccode_dump.txt")

print (file_name)    

# read file 
txt_in = open(file_name, 'r')