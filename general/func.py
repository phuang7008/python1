#!/home/ubuntu/workspace/local/bin/python
# In python, here is how you define a function; when you def a function, you define an object of type function
def hello(name) :
    print("Hello " + name)
    print("Welcome to Python")
    
hello('peter')

print("the type of the function hello")
print(type(hello))

# lambda function: the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called "lambda".
# lambda <input>: <expression>      
# here is the equivolent lambda function for the 'hello' function defined above. They produce exact the same results!
# Note that the lambda definition does not include a "return" statement -- it always contains an expression which is returned. 
g = lambda name: print("Hello " + name + ". Welcome to Python");      print(g('mark'));   print("The type of lambda function is ", type(g))

# Also note that you can put a lambda definition anywhere a function is expected, and you don't have to assign it to a variable at all.
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27];    print ("Lambda funcion often used with map() or filter() function\n", list(filter(lambda x: x % 3 == 0, foo)))

# Other useful build in functions: zip(), map(), filter(), reduce() etc. https://bradmontgomery.net/blog/pythons-zip-map-and-lambda/
# In python 3, all these utility functions were implemented in generator format, so you have to use list() function to cast them to print them

# zip() function takes two equal-length collections, and merges them together in pairs (tuple pairs).
a = list(range(1,6));     b = [2,2,9,0,9];    print("Created two lists, a and b\n", a, b);    z = zip(a, b);  print("Now zip(a, b) them together\n", list(z))

# map() function takes a function, and applies it to each item in an iterable (such as a list)  =>  map(some_function (eg lambda function, some_iterable)
lm = map(lambda pair: max(pair), zip(a, b));    print("Using lambda function inside a map() function to compare a and b list zipped by zip()\n", list(lm))

# The filter() function filter(func2, list) offers an elegant way to filter out all the elements of a list, for which the function func2 returns True. 
fib = [0,1,1,2,3,5,8,13,21,34,55];  print("filter odd nums in and even nums out\n", list(filter(lambda x: x % 2, fib)))

# The reduce() function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value (so don't use list() to cast).
from functools import reduce
x =[47,11,42,102,13];   print("Using reduce() to find the max num out\n", reduce(lambda a,b: a if (a > b) else b, x))

# if the list is empty, the reduce() function will give an error message. So you could supply an initial value to the reduce() call
y=[];       print("given initial value to prevent the error message\n", reduce(sum, y, 0))

# iterator: any object that allows you to loop through one by one is an iterator. It needs to implement __iter__ and __next__ functions
# 1). If we use it with a string, it loops over its characters. 2). If we use it with a dictionary, it loops over its keys.
# 3). If we use it with a file, it loops over lines of the file.

# generator function. it is a special type of iterator! To be considered an iterator, generators must define a few methods, one of which is __next__().
# to get the next value from a generator, we use the same built-in function as for iterators: next(). (next() takes care of calling the generator's __next__() method).
# The easiest way to remember what yield does is to think of it as return (plus a little magic) for generator functions.**



