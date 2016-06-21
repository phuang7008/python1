#!/home/ubuntu/workspace/local/bin/python

# In Python, functions are first class citizens, they are objects and that means we can do a lot of useful stuff with them.
# Therefore, when you def a function, you define an object of type function

# lambda function: the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called "lambda".
# lambda <input>: <expression>      
# here is the equivolent lambda function for the 'hello' function defined above. They produce exact the same results!
# Note that the lambda definition does not include a "return" statement -- it always contains an expression which is returned. 
g = lambda name: print("Hello " + name + ". Welcome to Python");      print(g('mark'));   print("The type of lambda function is ", type(g))

# Also note that you can put a lambda definition anywhere a function is expected, and you don't have to assign it to a variable at all.
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27];    print ("Lambda funcion often used with map() or filter()\n", list(filter(lambda x: x % 3 == 0, foo)))

# Other useful build in functions: zip(), map(), filter(), reduce() etc. https://bradmontgomery.net/blog/pythons-zip-map-and-lambda/
# In python 3, all these utility functions were implemented in generator format, so you have to use list() function to cast them to print them

# zip() function takes two equal-length collections, and merges them together in pairs (tuple pairs).
a = list(range(1,6));     b = [2,2,9,0,9];    print("Created two lists, a and b\n", a, b);    
z = zip(a, b);  print("Now zip(a, b) them together\n", list(z))

# map() function takes a function, and applies it to each item in an iterable (eg. a list)  =>  map(some_function (eg lambda function, a_iterable)
lm = map(lambda pair: max(pair), zip(a, b));    print("Using lambda function inside a map() to compare a and b list zipped by zip()\n", list(lm))

# The filter() function filter(f2, list) offers an elegant way to filter out all the elements of a list, for which the function f2 returns True. 
fib = [0,1,1,2,3,5,8,13,21,34,55];  print("filter odd nums in and even nums out\n", list(filter(lambda x: x % 2, fib)))

# The reduce() function reduce(func, seq) by continually applies the function func() to the sequence seq. 
# It returns a single value (so don't use list() to cast).
from functools import reduce
x =[47,11,42,102,13];   print("Using reduce() to find the max num out\n", reduce(lambda a,b: a if (a > b) else b, x))

# if the list is empty, the reduce() function will give an error message. So you could supply an initial value to the reduce() call
y=[];       print("given initial value to prevent the error message\n", reduce(sum, y, 0))
print()

#########################################################################################################################################
# *args and **kwargs ==> They are mostly used in function definitions. It allows you to pass different number of arguments to a function becuase 
# you do not know before hand that how many arguments can be passed to your function by the user so in this case you use these two keywords. 
# NOTE that it is not necessary to write *args or **kwargs. Only the * (or **) (asterisk) is necessary. 
# You could have written *var and **vars. Writing *args and **kwargs is just a convention. 
# https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/

# *args is used to send a non-keyworded variable (different) length argument list to the function.
def test_args(name, *args):
    print("Hello, " + name + " Welcome!")
    
    print("various arguments testing here or use a list, just remember to put * in front of the tuple or list")
    for arg in args:
        print(arg)

test_args("Harry", "29 yrs", "software developer", "from Shanghai", "Good sense of humor")
test_args("Ronnie", *("28 yrs", 'Singer', "Seattle", 'fighting'))
test_args("Peter",  *["48 yrs", 'Dancer', "Boston", 'Hiking'])
print()

# **kwargs allows you to pass keyworded variable length of arguments to a function. 
#You should use **kwargs if you want to handle named arguments in a function. 
def kw_args(name, **kwargs):
    print("Hello, " + name + " Welcome!")
    
    print("various keyworded arguments testing here, you can mixup dict with keyword items. Just remember to put ** in front of dict")
    if kwargs is not None:
        for key, val in kwargs.items():
            print(key + " is " + str(val))

kw_args("Jimmy", age=30, career="softare developer", **{'city':'Shanghai', 'earning':150000})
kw_args("Bernard", **{'age':45, 'career':'sell manager', 'city':'vancouver', 'kids':5})
print()

# if you want to use all three of these types of arguments (*args **kwargs and formal args) in functions 
# then the order is some_func(fargs,*args,**kwargs)

###################################################################################################################################
# user defined arguments: command line argument options and passing 
import argparse
def fibn(num):
    a, b = 0, 1

    for i in range(10):
        a, b = b, a+b
    return a
    
def Main():
    parser = argparse.ArgumentParser()
    
    # here are the position arguments, which don't need to use '-' format to specify. The program will grab them as the order given
    parser.add_argument("num", help="Please enter a number!", type=int)
    
    # here are the optional arguments, which do require the user to specify the option names using '-' notation
    # '-o' is for the shortcut, while '--output' is full option name. action. 
    # action='store_true' means return false if parameter doesn’t exist; return true if parameter exists.
    parser.add_argument("-o", "--output", help="Output results into a file!", action="store_true")
    
    # you could store option arguments in a group, such as mutually exclusive arguments (use one of them, but not both. give error if both used)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', help="given detail information", action='store_true')
    group.add_argument('-q', '--quiet', help="no detailed information given", action='store_true')
    
    # now grab the arguments from the command line
    args = parser.parse_args()
    result = fibn(args.num)
    
    # use the arguments using their corresponding labels and output the results based on the user options
    if args.verbose:
        print("The fibannacci number for " + str(args.num) + " is ", str(result))
    elif args.quiet:
        print(result)
    else:
        print("The result is ", result)
    
    if args.output:
        f = open('tt.txt', 'w')
        f.write("the result is " + str(result))

if __name__ == "__main__":
    Main()

###################################################################################################################################    
# python function decorator: http://thecodeship.com/patterns/guide-to-python-function-decorators/
# Essentially, decorators work as wrappers, modifying the behavior of the code before and after a target function execution, 
# without the need to modify the function itself, augmenting the original functionality, thus decorating it.

# Assign functions to variables
def greetings(name):
    return print ("Hello " + name)
some_greet = greetings("Kark");     # assignment

# Functions can be passed as parameters to other functions
def call_func(func):
    name1 = "John"
    return func(name1)
call_func(greetings)

# Functions can return other functions. In other words, functions generating other functions.
def myFunc():
    def getmessage():
        return "Hello World!"
    return getmessage
tmpFunc = myFunc()
print(tmpFunc())        # to invoke the call, use the tmpFunc(), not myFunc. Without (), nothing will be printed

# Define functions inside other functions; aka ===> Closures. A very powerful pattern that we will come across while building decorators.
# Closures are nothing but functions that are returned by another function. We use closures to remove code duplication. 
# Another thing to note, Python only allows read access to the outer scope and not assignment. 
def add_number(num):
    def adder(number):
        'adder add two numbers together. Here adder is a closure which adds a given number to a pre-defined one.'
        return num + number
    return adder
    
add_10 = add_number(10)
print(add_10(21));      print(add_10(39))    

# Composition of Decorators: 
# Function decorators are simply wrappers to existing functions. Putting the ideas mentioned above together, we can build a decorator.
'''
def get_text(name):
    return "I don't understand you, {0}, please just sit down!".format(name)

def p_decorator(func):                              # pass function as argument
    def func_wrapper(name):                         # inner function
        return "<p>{0}</p>".format(func(name))      # inner function pass the argument from outer function
    return func_wrapper                             # generate and return another function
tmpWrapper = p_decorator(get_text)                  # assign a function to a variable
print(tmpWrapper('Mary'))
'''  
'''
# Python's Decorator Syntax: Python makes creating and using decorators a bit cleaner and nicer for the programmer through some syntactic sugar 
# To decorate get_text we don't have to get_text = p_decorator(get_text) There is a neat shortcut for that, which is to mention the name of the 
# decorating function before the function to be decorated. The name of the decorator should be perpended with an @ symbol.
def p_decorator(func):                              # pass function as argument
    def func_wrapper(name):                         # inner function
        return "<p>{0}</p>".format(func(name))      # inner function pass the argument from outer function
    return func_wrapper                             # generate and return another function
    
@p_decorator
def get_text(name):
    return "I really like to talk to you, {0}, please have a drink!".format(name)
    
print(get_text("Cheery Face"))
'''

'''
# Now let's consider we wanted to decorate our get_text function by 2 other functions to wrap a div and strong tag around the string output.
def strong_decorator(func):
    def strong_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return strong_wrapper

def div_decorator(func):
    def div_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return div_wrapper 
    
def p_decorator(func):
    def p_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return p_wrapper 

# Here the order matters!!!    
@div_decorator
@p_decorator 
@strong_decorator 
def get_text(name):
    return "This is the new test for multiple decorations, {0}, come and enjoy!".format(name)

print(get_text("Stephen"))
'''

# The above example write three different wrappers only differ in tag names, why not put them into a single function to do all
def tags(tag_name):
    def tag_decorator(func):
        def wrapper(*arg, **kwargs):
            return "<{0}>{1}</{0}>".format(tag_name, func(*arg, **kwargs))
        return wrapper 
    return tag_decorator

@tags("div")
def get_text(name):
    return "This generic version is much better, {0}, what do you think?".format(name)

print(get_text("Nancy"))

# Use the new version of decorator inside a class method
class person(object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    @tags("p")    
    def get_name(self):
        return "%s %s" % (self.fname, self.lname)
        
personA = person("Joe", "Cherry")
print(personA.get_name())

###################################################################################################################################    
# functools: 
# Functions that operate on other functions. The functools module provides tools for working with functions and 
# other callable objects, to adapt or extend them for new purposes without completely rewriting them.

# The above decorator could further enhanced through functools module.  functools module contains functools.wraps. 
# Wraps is a decorator for updating the attributes of the wrapping function(func_wrapper) to those of the original function(get_text). 
# This is as simple as decorating func_wrapper by @wraps(func). Here is an example:

from functools import wraps

def tag2(tag_name):
    def tag_decorator(func):
        @wraps(func)
        def wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return wrapper 
    return tag_decorator 

@tag2("strong")
def get_text2(name):
    'This is the main function'
    return "Using functools wraps for decoration. {0}, Do you need it?".format(name)

print(get_text2("Money Money Money"))
print(get_text2.__name__);      print(get_text2.__module__);        print(get_text2.__doc__)

# functools.partial: http://www.pydanny.com/python-partials-are-fun.html
# It does two things: Makes a new version of a function with one or more arguments already filled in. New version of a function documents itself.
def power(base, exponent):
    return base ** exponent
    
p1 = power(2, 4);       print("power 4 for base 2 is ", p1)

# what if you want to define a new function with base decided, such as 2, 4, 7 etc
from functools import partial

power2 = partial(power, base=2)
power4 = partial(power, base=4)
power7 = partial(power, exponent=7)

print("power 7 on base 3 is ", power7(3));      print("power 5 of base 4 is ", power4(5))








