#!/home/ubuntu/workspace/local/bin/python

# Using generator to read in fasta file
def parser(file):
    fh = open(file, 'r')
    for line in fh:
        if ('>' in line):
            print("\nnew record")
        else:
            # .strip() by default removes all whitespace at the start and end, including spaces, tabs, newlines and carriage returns. 
            # Leaving it in doesn't do any harm, and allows your program to deal with unexpected extra whitespace inserted into the file.
            # strip(chars)  # will strip chars from both start and end
            # lstrip() and rstrip() will strip whitespaces from 'left' or 'right' respectively by default
            yield line.strip()
            #yield line
            #yield line.strip("\n\t")
    fh.close()

fhg = parser('test.fa')
print("Generator for reading fasta file\n", fhg)
for line in fhg:
    print(line, end='')
print()

# write to a file
def toWrite():
    f = open('myFile.txt', 'w')
    for i in range(4):
        f.write(input("Please enter a word: ") + "\n")
        #f.write("Information added into file" + "\n")
    f.close()

toWrite()
print()

# using 'with' statement for file write
def toWrite2():
    words = [1,55, 'test', 4.567, None, True, 'More...']
    with open('myFile.txt', 'w') as f:
        for wd in words:
            f.write(str(wd) + "\n")
    # here you don't need to close it as with handle it for you automatically
toWrite2()
print()

# Access the webpage using Python IO
import urllib
import re

try:
    from urllib.request import urlopen
except:
    pass

# if you use the same regular expression over and over through a loop, you might want to compile the regular expression first to speed up
pat = re.compile(r'<title>+.*</title>+', re.M|re.I)
sites = "google yahoo cnn msn".split()
for s in sites:
    print("Searching: " + s)
    try:
        u = urlopen('http://' + s + '.com')
    except:
        u = urllib.request.urlopen('http://' + s + '.com')
        
    text = u.read()
    title = re.findall(pat, str(text))
    print(title[0])
