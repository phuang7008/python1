#!/home/ubuntu/workspace/local/bin/python

# iterator: any object that allows you to loop through one by one is an iterator. It needs to implement __iter__ and __next__ functions
# __iter__ returns the iterator object itself. This is used in for and in statements.
# __next__ returns the next value from the iterator. If there is no more items to return then it should raise StopIteration exception.
class reverse(object):
    # this is to reverse the string from the input and output a string in reverse order
    def __init__(self, phrase):
        self.phrase = phrase;
        self.length = len(phrase)
        
    def __iter__(self):
        return self;
        
    def __next__(self):
        if self.length == 0:
            raise StopIteration
        else:
            self.length -= 1
            return self.phrase[self.length]
            
rev = reverse("Thank you very much")
for c in rev:
    print(c, end=' ')
print()

# More about iterator
# 1). If we use it with a string, it loops over its characters. 2). If we use it with a dictionary, it loops over its keys.
# 3). If we use it with a file, it loops over lines of the file.

# generator function. it is a special type of iterator! To be considered an iterator, generators must define a few methods, 
# one of which is __next__(). to get the next value from a generator, we use the same built-in function as for iterators: next(). 
# (next() takes care of calling the generator's __next__() method).
# The easiest way to remember what yield does is to think of it as return (plus a little magic) for generator functions.**
def myGenerator(*args):
    for arg in args:
        yield arg

print("myGenerator function's output: ", list(myGenerator('peter', 'plays', 'basketball')))

# now using generator to re-implement the reverse class
class reverse2(object):
    
    def __init__(self, phrase):
        self.phrase = phrase
        self.length = len(phrase)
    
    # Any class with a __iter__ method which yields data can be used as a object generator.    
    def __iter__(self):
        while self.length >= 1:
            self.length -= 1
            yield self.phrase[self.length]
    
rev2 = reverse2("Game of Thrones Season 6")
print(rev2.length)
for c in rev2:
    print(c, end=" ")

print()  

# Generator expressions
# The syntax of generator expression says that always needs to be directly inside a set of parentheses and cannot have a comma on either side.
squr = (x*x for x in range(1,20));      print("Using Generator expression to create a list on the fly and get results when needed\n", list(squr))
    
f = (line for line in open('align.dnd', 'r'))
print("first line (need to strip the newline and carriage return)\n",  next(f).strip("\n\t"));        
print("Second line (need to strip the newline and carriage return)\n", next(f).strip("\n\t"))

# Using generator to read in fasta file
def parser(file):
    fh = open(file, 'r')
    for line in fh:
        if ('>' in line):
            print("\nnew record")
        else:
            yield line.strip("\n\t")
    fh.close()
    
fhg = parser('test.fa')
print("Generator for reading fasta file\n", fhg)
for line in fhg:
    print(line, end='')

print()









