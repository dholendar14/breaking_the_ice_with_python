"""
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use init method to construct some parameters
"""
class InputOutString():
    def getString(slef):
        slef.s = input()
    
    def print_string(slef):
        print(slef.s.upper())
    
x = InputOutString()
x.getString()
x.print_string()