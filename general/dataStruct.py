#!/home/ubuntu/workspace/local/bin/python

# in python, sequence types include String, List, Tuple. It allows many operations such as indexing, slicing, addition/multiplication
# append/concatenation, iteration, checking membership (in/not in), sorting, count, length (len()), max/min/sum etc.
# For slicing, the syntext is [start : end+1 : step] and they all optional.

# Square bracket [] is used for list object (sequence type), which is mutable and sortable. Therefore, it is not hashable
a = [2,5,6, "test", True, 2, 5, 5, 5, 2, 5];        print("python mutable list: ", a);  
aa = a;         print("This is a shollow copy, which means they point to the same thing: aa = a; ", aa)
aaa = a[:];     print("This is a deep copy, which will create a new list with the same elements as a => aaa = a[:]; ", aaa);
a[2] = "me";    print("change 3rd value in a: ", a);      print("The values of aa is ", aa);  print("The value of aaa deep copy is ", aaa);
a.append(None); print("using append() to add a value ", a);     print("or using + sign", a+aa);    print("Slicing: ", a[1:4]);     
ab = a * 3;     print("multiplication: ", ab);      print("length of a: len(a) ", len(a));   print("min of a: min(aaa[0:3]) ", min(aaa[0:3]))
al = list(range(1,30,3));   print("Create a range() and cast it using list to create a list", al)
print("To count number of occurrence of 5 use: a.count(5)\n", a.count(5))
print()

from collections import Counter
a = ['2',5,6, "test", True, '2', 5, 5, 5, '2', 5];
print("To produce the occurrence of all items: Counter(a)\n", Counter(a))
print("if you only want values not keys, use Counter(a).values()\n", Counter(a).values())
print("output the first two most common ones in the list a -> Counter(a).most_common(2)\n", Counter(a).most_common(2))
print("You can use elements() to find all the key items in a counter: Counter(a).elements()\n", Counter(a).elements())

# you could perform various arithmatic operation and set operations on two Counters
a2 = Counter('abcabcccdce1222564');     print("new Counter\n", a2)
print("Addition of two Counters Counter(a) + a2\n", Counter(a) + a2)
print("Substraction of two Counters Counter(a) - a2\n", Counter(a) - a2)
print("Union of two Counters Counter(a) & a2\n", Counter(a) | a2)
print("Intersect of two Counters Counter(a) + a2\n", Counter(a) & a2)
print()

# deque: a type of sequence container. A double-ended queue, or deque, supports adding and removing elements from either end. 
# The more commonly used stacks and queues are degenerate forms of deques, where the inputs and outputs are restricted to a single end.
import collections
d = collections.deque("abcabcdefg");    print("Create a deque: d = collections.deque('abcabcdefg')\n", d)
print("you could index it from left and right d[1] and d[-2] and len(d)\n", d[1], d[-2], len(d))

# A deque can be populated from either end, termed “left” and “right” in the Python implementation. 
d.extend('hnp');      print("using extend() to extend the deque (default at right side) by splitting them up\n", d)
d.append('itz');      print("using append() to add item to the deque (default at the right side) by adding as a single item\n", d)

d.extendleft('jry');  print("using extendleft() to extend the deque at the front end by splitting them up in reverse order\n", d)
d.appendleft('kmx');  print("using appendleft() to append the deque at the front end by adding all them in as a single item\n", d)

# you could use pop() from right hand side or popleft() remove from left side
# Since deques are thread-safe, the contents can even be consumed from both ends at the same time from separate threads.
d1= d.pop();    d2= d.popleft();    d3= d.popleft();    print("Remove items from either ends using pop() or popleft()\n", d, d1, d2, d3)

# Rotating: Another useful capability of the deque is to rotate it in either direction, to skip over some items.
d.rotate(3);    print("move around items in the deque using d.rotate(3)\n", d)
d.rotate(-2);   print("using rotating again using negative index d.rotate(-2)\n", d)
print()

# sortedcontainers: in order to use it, you need to install 'sudo pip install sortedcontainers'
from sortedcontainers import SortedList
sl = SortedList(['a', 'q', 't', 'c', '55', '23', '19', '78']);      print("Created a SortedList (all need to be of the same type): \n", sl)
sl.add('m');    del sl[0];      print("Deletion and Addition will still maintain the sorted order\n", sl)
print(); 

# need to define a function for usage
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        
for item in aaa:  # iteratte through item aaa
    if is_number(item):
        print(item, end="  ") 
        
for index, item in enumerate(aaa):     # if you need both index and item, you need to use enumerate() function
    print(index, "  ", item, end="  ")
    
# here is the List specific functions. Be careful here as the append(), insert(), del() and sort() are destructive operation 
# (they modify the list in place instead of of returning a new list). if you used them with print(), they will return None
# therefore, you need to do it outside the print to make the results show up.
an = [ m for m in range(8) if m > 3];    print("using list comprehension ", an);    an.insert(1, 201); print("an.insert(1,11) is ", an)
ann = an[:];   print("Deep copy here for ann = an[:], ", ann);  an.sort();  print("an.sort() will put items in the an in sorted order ", an);
an3 = sorted(ann);      print("the sorted() returns a new list without change the original list ", an3);     print("the original list is ", ann)
print("a.pop() the last item of the list, which is  ", a.pop())
print()

####################################################################################################################################
# parenthesis () is used for tuple objects (sequence type), which is not mutable. So it is hashable. using a comma for 1 or more elements, 
# with parenthesis being optional in many contexts. For single element, you have to put a comma in, otherwise, you will get a scalar value
b = ('this is a string', [29, 'test', 78], 1, 44);         print("Create a tuple, which is immutable: ", b);
print("but you could append thing for tuples b += (3,)");     b += (3,);   print(b);      print("OR b +='55', ");    b+= '55',;      print(b)
print("Access single element through indexing: b[2] \n", b[2], b[1][0]);
b[1][0] = 'changed';     print("You could change the content of a list inside a tuples b[1][0] = 'changed', but you can't delete the list\n", b)

# For a single member, if you don't put comma, at very end, it is just like regular assignment operation
b = (5);        print("no comma, which is just a value, not a tuple b = (5): ", b);  print()

# namedtuple: A namedtuple assigns names, as well as the numerical index, to each member. https://pythontips.com/tag/python/
# With namedtuples you don’t have to use integer indexes for accessing members of a tuple. 
# You can think of namedtuples like dictionaries but unlike dictionaries they are immutable.

from collections import namedtuple

# ===> Important: Each kind of namedtuple is represented by its own class, created by using the namedtuple() factory function. 
# ===> Important: The arguments are the name of the new class and a string containing the names of the elements.
# A namedtuple has two required arguments. They are the tuple name and the tuple field_names.
# In the following example the tuple name was ‘Animal’ and the tuple field_names were ‘name’, ‘age’ and ‘type’.
# the field_names could be 'renamed' if there is a conflict with the python keywords or duplicated field_names (age age) => (age, _1)
Pet = namedtuple("Animal", "name age type", rename=True)
perry = Pet(name="Snow", age=12, type='Dog')
print("The namedtuple perry is \n", perry);     print("name of perry is ", perry.name);     
print("class type is type(perry)\n", type(perry));      print("The field names of the perry.fields is ", perry._fields)

# However, do remember that as with tuples, attributes in namedtuples are immutable. 
print("You can't do the assignment like perry.age = 15")

# You should use named tuples to make your code self-documenting. They are backwards compatible with normal tuples. 
# It means that you can use integer indexes with namedtuples as well:
print("Accessing through indexing perry[2]\n", perry[2])

# Last but not the least, you can convert a namedtuple to a dictionary. Like this:
peddy = perry._asdict();     print("Convert perry to a dict like peddy = perry._asdict() \n", peddy)

# OR you could use the following format to assign a namedtuple
Person = namedtuple("People", ['name', 'age', 'rank'])
Johnny = Person(name='John', age=43, rank='freelance');     print("Person Johnny's information is \n", Johnny);     print(Johnny.name)

# you could loop through any tuples (either regular tuple or named tuple) using the following approach
for p in [perry, Johnny]:
    print("name is %s at the age of %d with some additional information %s" % p )
    
print()

####################################################################################################################################
# String is a type of sequence. All the operation mentioned below also work for Lists and Tuples
x = 'computer';     print(x);   print("indexing 'computer', x[3]: ", x[3]);      print("Slicing: x[1:6:2] ", x[1:6:2]);  
print("Item 3 to end: x[3:] ", x[3:]);  print("Item 0-4: x[:5] ", x[:5]);    print("Negative indexing: last item x[-1] ", x[-1]);  
print("Last three item: x[-3:] ", x[-3:]);  print("Everything except Last two items: x[:-2] ", x[:-2]);   
print("Multiplication: x * 4 ", x * 4);    print("membeship checking: 'u' in x: ", 'u' in x);     print("max letter: max(x)", max(x)); 
print("count letters: x.count('p') is ", x.count('p'));     print("sorted(): ", sorted(x));    print("index(x): ", x.index('p'));     print()

####################################################################################################################################
# Curly braces {} create dictionaries (hashes unordered) or sets. Note items in dict are in random order
d1 = {'foo' : 42, 'bar' : 39, 'play' : 90, 'hi' : 34};       print ("creating a hash (or dict)");        print(d1);       print(d1['foo'])
d1['beef'] = 25.5;      print("adding new item to the dict: ", d1);     del d1['beef'];     print("delete an item 'beef' from the dict: ", d1)
print("find the len() of the dict d1 ", len(d1));   print("check membership, only checking keys, not values ", 'foo' in d1)
d2 = {c:ord(c) for c in x};     print("Using dict conprehension to create a dictionary ", d2)

# some useful dict operations, and they are very useful for iterate through the dict
print("get all keys, d1.keys() is ", d1.keys());   print("get all values, d1.values() is ", d1.values());   
print("get key-value tuple pairs, use d1.items() ", d1.items());    print("check membership for a value: 42 in d1.values() is ", 42 in d1.values())
print("Keys are: ", end = "  ")
for k in d1.keys():
    print(k, end="  ")
print()

print("key-value pairs are ", end="  ")
for k, v in d1.items():
    print(k,'-', v, end="    ")
print()

print("clear all in d1.clear() ", d1.clear());      print("to delete the entire dict, use del d1");     del d1;
print()

# sortedcontainers
from sortedcontainers import SortedDict
sd = SortedDict(zip('dglkjuc', range(6)));      print("Created a SortedDict and all keys are in sorted order: \n", sd, list(sd.keys()))
del sd['g'];    sd['qq'] = 11;      print("Deletion and Addition, the keys are still sorted:\n", sd, list(sd.keys()))
print()

####################################################################################################################################
# Sets are collections of unique elements and you cannot order them. But you can use set operations on them
s1 = set([1, 2, 2, 4, 5, 6, 6]);     print("Creating a set using set(). Note there is no repeat element", s1);
sc = { x**2 for x in range(8) if x > 3};     print("Using set comprehension to create a set: ", sc)
s2 = set(aaa);      print("type cast a list to create a set s2=set(aaa) is ", s2);    s2.add("added");  print("add() an item: ", s2)
s2.remove('added'); print("now remove() the member item (not index) just added: ", s2); print("the len(s2) of the set is now ", len(s2))
print("check membership 'test' in s2 ", 'test' in s2);      print("check membership not in the list: 'test' not in s2 ", 'test' not in s2)
print("s2.pop() random item from s2 set ", s2.pop());       print("to s2.clear() to delete all items in the set s2 ", s2.clear())
s3 = sorted(s1, reverse=True);        print("you can NOT use s1.sort() for sorting, to sort, use sorted(s1, reverse=True) a set: ", s3);

# set math set operations
s2 = set(aaa);  print("s1 and s2 are ", s1, s2);    
ss = s2 & s1;   print("set intersection (here True is evaluated to 1: s2 & s1 is", ss);   ss = s1 | s2;   print("set union s1 | s2 is ", ss);     
ss = s1 ^ s2;   print("set symmetrical difference: s1 ^ s2 is ", ss);   ss = s2 - s1;   print("set difference, in s2 but not in s1 is", ss);    
ss = s2 <= s1;  print("subset, s2 contains s1 ", ss);       s2.add(4);  ss = s2 >= s1;  print("superset s2 contains s1 ", ss)  
print()

# sortedcontainers
from sortedcontainers import SortedSet
ss = SortedSet('dcabefjkll');       print("Create a SortedSet:\n", list(ss), 'k' in ss)
ss2 = ss | 'sfdjk';     ss3 = ss & 'dcgve';     print("using set operations: \n", ss2, ss3)
print()

####################################################################################################################################
# generator has been heavily used in anything that could iterates. To implement generator, you need keyword 'yield' or generator comprehension
g = (i for i in x);     print("Using generator comprehension: ", g);    print("Obtain next item using next() ", next(g))
for i in g:
    print("The value is ", i, ";", end=" ")
print()

# generator function
def my_func(x):
    #while True:
    for i in x:
        yield ord(i)

my_val = my_func(x);    # to get my_val out, you need to loop through it, as it is a generator now
for i in my_val:
    print("Value is ", i, ";", end="  ")
print()

# or you could use generator comprehension
my_val = (ord(i) for i in x);       print("Get next ", next(my_val))
print()

# note, you can't pass a generator to a matplotlib.pyplot, as it will convert everything into a numby array under the hood
# and numpy arrays require their sizes to be known up-front. Thus you can't pass in a generator because you don't know the 
# size of data that a generator holds. range() is an except as it provides many facilities to help determine the size
import numpy as np
import matplotlib.pyplot as plt
print("The following would fail: plt.plot(my_val, range(x))"); 