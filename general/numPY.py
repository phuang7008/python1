#!/home/ubuntu/workspace/local/bin/python

# this file contains information about numpy and scipy; # there are different ways to import modules. 
# In script, you will like to import every module explicitly because it is easier for others to read your code
from numpy import array

# in the iPython Notebook or in the command line, sometimes you will see the following, which include everything
from numpy import *

# however, there is another way to import numpy in script and it is quite good as well
import numpy as np

# for plot in cloud 9, you need to do the following to make it work (yes, it works in here)
# The canonical renderer for user interfaces is Agg which uses the Anti-Grain Geometry C++ library to make a raster (pixel) 
# image of the figure. All of the user interfaces except macosx can be used with agg rendering, e.g., WXAgg, GTKAgg, QT4Agg, TkAgg. 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt     ### Do not do this prior to calling use()

a = array([1,2,3,4,5,6,7]);     b = array([2,3,4,5,6,7,8]);    print("Creating numpy array using array() ", a, b)
c = a + b;      print("adding two arrays together using +; the results is not like list concatenation. it's elem-wise addition:", c);
d = a * b;      print("array multiplication is also done element by element " , d)
e = a ** b;     print("array power is also done element by element " , e)
f = a + 2;      print("You could add a scalar value to evey element in an array (broadcase to everyone) a + 2", f)
print()

a = arange(21); print("Use arange() which likes range(), but it produces array (not list) with the range specified; ", a)
a = arange(21) * 2 * pi / 21; print("more arange() with multiplication and division by scalar(s) ", a)
a = np.arange(2,40,2);  print("Using user defined range with stepwise of 2 ", a)
print()

################################################################################################################################
# to plot a graph, You can create a figure the usual way, except save it in cloud 9
# note: in command, when you plot a graph, it will show right away. However, in the script, you have to use show() to diplay it
fig, ax = plt.subplots(1, 1);    b = sin(a);     print("plot is save as .svg file, use preview to view the dp.svg file");  
ax.hold(False);  print("You only need to call ax.hold(False) once and the system will remember the setting; to turn it back on; call ax.hold(True);")
ax.plot(a, b);   fig.savefig("dp.svg");   print("Now clear figure");    #plt.gcf().clear();
print()

# use matplotlib for plot. you could use ?plot to find out various format plot uses
x = linspace(0, 2*pi, 50);      print("linspace(0, 2*pi, 50) values are: ", x); 
ax.plot(x, sin(x)); fig.savefig("dp.svg");
ax.plot(x, sin(x), x, sin(2*x));    fig.savefig("dp.svg");  print("You could add multiple graphs in the same figure using (xi, yi)");
ax.plot(x, sin(x), 'r-^');   fig.savefig("dp.svg");   print("print graph using 'r-^' (red, dot-dash, triangle) line format!");
ax.plot(x, sin(x), 'b-o', x, sin(2*x), 'r-^' );   fig.savefig("dp.svg");

# scatter plot
plt.title("interactive test");  plt.xlabel("index");    #plt.colorbar()
ax.scatter(x, sin(x));  fig.savefig("dp.svg");
#ax.hist(np.random.randn(2000, 5));     fig.savefig("dp.svg");

################################################################################################################################
# more array
a = np.array([[2,5,7,1,9,15], [4,99,3,72,17,5]]);   print("Create a 2 dimension array: ", a);  print("type of a is: ", type(a))
print("data type of a: a.dtype is ", a.dtype);      print("the item size of a is a.itemsize ", a.itemsize);     print("shape of a is ", a.shape)
print("size of a (number of elements) is a.size ", a.size);     print("Number of bytes using nbytes ", a.nbytes);   
print("the dimension a.ndim is ", a.ndim);      

# indexing and slicing
s = np.array(range(100));   print("Generate an array without dimension: ", s);  s.shape = (10,10);   print("new array is ", s)
print("array indexing s[0][4] is ", s[0][4]);   print("OR using s[0, 4] ", s[0, 4]);    s[0, 2] = 77;   print("assign new value a[0, 2] = 77 ", s[0, 2])
print("Slicing: s[0:1, 2:-2] (s[1:3][1:-2] won't work here) ", s[0:4, 2:-2]);     
b = a;  b.fill(5);  print("reset everything in b to 5 using b.fill(5) ", b);    b[:] = 2;   print("reset everything to 2 using b[:] ", b)

# be careful about silence coersion in array assigment
b[1][3] = 10.6;     print("coersion will force numeric to integer b[1][3] = 10.6 is ", b[1][3]); b.fill(4.8);   print("b.fill(4.8) all become 4 ", b)

# math
print("Mean of the entire array: ", np.mean(s));    print("mean of each column (axis=0) are ", np.mean(s, axis=0))
print("mean of each row (axis=1) are ", np.mean(s, axis=1))

# in order to insert nan value into the s, I need to convert the integer array s into a float array using astype
s = s.astype(float);    s[2,3]=nan;     s[1,5]=nan;     s[4,2]=nan;    print("float type array s ", s);   
print("produce some missing data and the mean calculation will fail ", np.mean(s))
print("we need to mask it first to do the calculation. s2 = np.ma.masked_array(s, np.isnan(s))");      s2 = np.ma.masked_array(s, np.isnan(s));
print("Once it is masked, you could try to do the calculation again ", np.mean(s2))

# file input and output
# Using numpy module
data = np.loadtxt('file', skiprows=n);      print("using loadtxt() for reading file if there is no missing data!")
gDat = np.genfromtxt('', delimited=',', skiprows=n);     print("Read from a txt file with comma delimited if there are missing data!")
lDat = np.load();
fDat = np.fromfile();       print("Loading binary file in! if sep=' ' is not empty, it is text file! sep='' if a binary file")

# Using regular open file from standard library
fh = open('file', 'r');     print("if you want to parse header information ")
for idx, line in enumerate(fh):
    if i is n: break
    print("do other things here")
    line.strip().split('\t')
fh.close()

# Using build-in csv module
import csv
csv1 = open('file', 'tb')
data = csv.reader(csv1, delimited='\t');
table = [row for row in data]



