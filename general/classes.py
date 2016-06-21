#!/home/ubuntu/workspace/local/bin/python

# Python is an OO language. So you could write classes! encapsulation
# Each class has its own properties (ie attributes) and functions on how to handle its property. Outside world can't not touch its internal properties
# Note: The first argument of every class method, including __init__, is always a reference to the current instance of the class. 
# By convention, this argument is always named self. (NOTE: self is not reserved keyword in Python)
class Employee(object):
    'Common base class for all employees'
    empCount = 0        # The variable empCount is a class variable whose value is shared among all instances of a this class.
    
    # class constructor or initialization method that Python calls when you create a new instance of this class.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print("Total number of employees is %d" % Employee.empCount)
        
    def displayEmployee(self):
        print("Current Employee is ", self.name + " And the salary is " + str(self.salary))
        
    # abstract method
    def code(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    
    # Python has two different ways to convert an object to a string: str() and repr(). Printing an object uses str(); printing a list 
    # containing an object uses str() for the list itself, but the implementation of list.__str__() calls repr() for the individual items  
    # So you should also overwrite __repr__(). A simple __repr__ = __str__ at the end of the class body will do the trick.
    
    # __str__ method is a special function that is defined for all classes in Python. It returns the string representation of an object. 
    # It is called by the str() function and by the print statement to display the "informal" string representation of an object.
    # Implement __str__ for classes which you think readability is more important of non-ambiguity.
    def __str__(self):
        return ("%s earns %d" % (self.name, self.salary))
    
    # __repr__ is called by repr() to display the "official" string representation of an object. in most cases, it's the same as __str__ function 
    # if __repr__ is defined, and __str__ is not, the object will behave as though __str__=__repr__.
    # Therefore, Implement __repr__ for every class you implement. There should be no excuse.
    #__repr__ = __str__
    def __repr__(self):
        return ("%r earns %r" % (self.name, self.salary))
        

nancy = Employee('Nancy', 55000)
gary  = Employee('Gary', 54000)

nancy.displayEmployee()
print("str() calls the __str__ function inside the class: str(nancy)\n", str(nancy))
print("using print(nancy) also produce the same results");    print(nancy)    
print("Total number of emplayees are %d" % Employee.empCount)

#You can add, remove, or modify attributes of classes and objects at any time 
nancy.age = 29      # Add an 'age' attribute.
nancy.age = 45      # Modify 'age' attribute.
del nancy.age       # Delete 'age' attribute.

# Instead of using the normal statements to access attributes, you can use the following functions to access the newly added attributes
hasattr(nancy, 'kid');      print("check if the attribute exist, ", hasattr(nancy, 'kid'))      # Returns true if 'age' attribute exists
setattr(nancy, 'kid',  1);  # Set attribute 'kid' at 8
getattr(nancy, 'kid');      print("Get the attribute for nancy's kid", getattr(nancy, 'kid'));  # Returns value of 'age' attribute
delattr(nancy, 'kid');      print("Delete the attribute for nancy's kid")           # Delete attribute 'age'

print()

# Inheritance
# Instead of starting from scratch, you can create a class by deriving it from a preexisting class by listing the parent class 
# in parentheses after the new class name. The child class inherits the attributes of its parent class, and you can use those attributes 
# as if they were defined in the child class. A child class can also override data members and methods from the parent.
import random
class Manager(Employee):
    
    def __init__(self, name, salary, rank):
        self.rank = rank
        super().__init__(name, salary)       # the main advantage using super() comes with multiple inheritance
    
    # implement the base abstract method
    def code(self):
        print("The secret code for you is :", random.randint(0,50))
    
    # Method overriding    
    def __str__(self):
        return super().__str__() + ', ' + self.rank
        
peter = Manager('Peter', 79000, 'ABC')
chris = Manager('Chris', 110000, 'CEO')
chris.code()

print("Total number of employees is ", Employee.empCount)
print(peter, "\n", chris)





