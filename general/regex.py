#!/home/ubuntu/workspace/local/bin/python
# this files contain all the regular expression related subject

# The module re provides full support for Perl-like regular expressions in Python. 
import re

line = "Cats are smarter than dogs, and I disagree, they both smart"
pat = re.compile(r'(\w+) are (.+) .*', re.M|re.I)

# re.match() and re.search() will allow you to capture the found items inside the () with index starting from 0.
# you could use the group(index) function to find each one of them. Or use groups() to find all captured items.
matchObj = re.match(pat, line)
searchObj = pat.search(line)

splitedObj = re.split(r'\s*', line, re.M|re.I)  

# if you use (\s*) with parenthesis, it will output individual whitespace as well
splitSpace = re.split(r'(\s*)', line, re.M|re.I) 

if matchObj:
    print("matchObj group() is: ", matchObj.group())
else:
    print("There is no match!")
    
if searchObj:
    print("searchObj groups() is: ", searchObj.groups())
else:
    print("There is no match!")

print("regex split line into words as \n", splitedObj)
print("regex split line into words and space char as \n", splitSpace)

# if you use the same regular expression over and over through a loop, you might want to compile the regular expression first to speed up
import urllib
try:
    from urllib.request import urlopen
except:
    pass

sites = "google yahoo cnn msn".split()
pat = re.compile(r'<title>+.*</title>+', re.M|re.I)

for s in sites:
    print("Searching: " + s)
    try:
        u = urlopen('http://' + s + '.com')
    except:
        u = urllib.request.urlopen('http://' + s + '.com')
        
    text = u.read()
    title = re.findall(pat, str(text))
    print(title[0])

# Need to do some text file process to find the matched items
string1 = "ACAATTCTTATAGTTATA"

pat1 = re.compile(r'[actgACTG]', re.M|re.I)
fh = open('WebPage.txt', 'r')
for line in fh:
    matches = re.findall(pat1, line)
    
    # join is a string method, you need to invoke it using string object. here I use str1
    str1 = ''.join(matches).upper()
    if (str1 == string1):
        print("Using findall() r'[actgACTG]' ", str1)
fh.close()

pat2 = re.compile(r'[^actgACTG]*', re.M|re.I)
fh = open('WebPage.txt', 'r')
for line in fh:
    matches = re.sub(pat2, '', line)
    str2 = ''.join(matches).upper()
    if (str2 == string1):
        print("Using sub() r'[^actgACTG]*' ", str2)
fh.close()

pat3 = re.compile(r'[^actgACTG]*', re.M|re.I)
fh = open('WebPage.txt', 'r')
for line in fh:
    if len(line.strip()) == 0:
        break
        
    matches = re.split(pat3, line)
    str2 = ''.join(matches).upper()
    if (str2 == string1):
        print("Using split() r'[^actgACTG]*' ", str2)
fh.close()

pat4 = re.compile(r'A|C|T|G', re.M|re.I)
fh = open('WebPage.txt', 'r')
for line in fh:
    matches = pat4.findall(line)
    str1 = ''.join(matches).upper()
    if (str1 == string1):
        print("Using findall() with  r'A|C|T|G' ", str1)
fh.close()

# There are other pattern matchings such as lookahead lookbehind etc. But they are more complicated