#!/home/ubuntu/workspace/local/bin/python
# https://mkaz.blog/code/python-argparse-cookbook/

# use the traditional C type argument passing: sys.argv array (list) which contains all the argument passed in
'''
import sys

if (len(sys.argv) > 1):
    print("First item in sys.argv[0] is ", sys.argv[0])
    print("Second item (argument) passed is sys.argv[1] ", sys.argv[1])
    print("The last item passed in is sys.argv[-1] ", sys.argv[-1])
    print("all the arguments passed in is sys.argv[1:] ", sys.argv[1:])
'''

# use argparse module for Flag Parameters or named parameters or variable length arguments
# A great thing about using argparse is you get built-in help. You can try it out by passing in an unknown parameter, -h or --help
# A side effect of using it, an error occurs if users pass in a command-line argument not expected, this includes flags or just an extra argument.
import argparse

# Create an instance of ArgumentParser object
parser = argparse.ArgumentParser(description='Demo')

# Add arguments
# The action parameter tells argparse to store true if the flag is found, otherwise it stores false.
# Either short '-' or long flag (--fullName) could be used
parser.add_argument('-v', '--verbose', help="Verbose flag", action='store_true')

# Required Flags: You can make a flag required by setting, required=True this will cause an error if the flag is not specified
# Variable Type: you could specify the type to be used with a specific argument. If type doesn't match, error will occur
parser.add_argument('-L', '--limit', required=True, type=int)

# Positional Arguments: arguments specified without flags
# File Types: Argparse has some built in filetypes which makes it easier to open files specified on the command line. 
# Here's an example writing a file, you can do the same reading a file.
parser.add_argument('filename', help="Filename is needed for storing data!", type=argparse.FileType('w'))

# How argparse determines the Number of Arguments? Argparse determines the number of argument based on the action specified
# for our 'verbose' example above, the store_true action takes no arguments, as it's just a boolean true or false
# By default, argparse will look for a single argument, for example the filename example shown above.

# If you want your parameter to accept a list of items, you can specify nargs=n for how many arguments it will accept.
# However, it might create unexpected result when use positional parameters. It is recommended you use nargs with flag arguments
parser.add_argument('nums', nargs=3, type=float, help="Please specify three numeric numbers!")

# Variable Number of Parameters: The nargs argument accepts a couple of extra special parameters such as '*' (0 or more) or '+' ( 1 or more). 
# If you want the argument to accept all of the parameters, you can use * which will return all parameters if present, or empty list if none.
parser.add_argument('-p', "--point", nargs='*', help="vector points (x, y) coordinates", type=float)

# You can also specify nargs='?' if you want to make an argument optional, but you need to be careful how you combine ? and * parameters, 
# especially if you put an optional positional parameter before another one.

# Default Value: You may specify a default value if the user does not pass one in. Here's an example using a flag.
parser.add_argument('--top', type=int, default=100, help="Specify max int value for top. default=100!")

# Remainder: If you want to gather the extra arguments passed in, you can use remainder which gathers up all arguments not specified into a list
# parser.add_argument('args', nargs=argparse.REMAINDER)

# Choices (Enumerator): If you only want a set of allowed values to be used, you can set the choices list, which will display an error if invalid entry.
parser.add_argument('throw', choices=['rock', 'scissors', 'paper'])

# grab all the arguments
args = parser.parse_args()


print("-Verbose argument is ", args.verbose)
print("-L or --limit argument is ", args.limit)
print("Filename specified is ", args.filename)
args.filename.write("This file opened for writing")

print("Positional argument nums is ", format(args.nums))
print("Positional argument point with variable number of parameters ", format(args.point))
print("The optional argument top value is ", args.top)
#import time
#time.sleep(10)
#print("Grab all the remainder arguments ", args.args)
print("Choices used is ", args.throw)

