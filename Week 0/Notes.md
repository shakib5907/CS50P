# CLI commands

**code fileName.py** - to create a new file

**pyhton fileName.py** - to run that file (to run the code)

# Quick Notes

**f string** - print(f"") - using f string, variables can be used inside of a print function more conveniently. We just have to use a curly barces to use a variable {}

The **print** function actually takes 3 parameters - print(\*objects, sep = ' ', end = '\n') -> end parameter is causing a new line everytime we use it. Making end = '' will allow us to use a print function but not going to a new line. sep = ' ' causes a separation in a line, works as a space. Making sep = '' will allow 2 or more variables or strings to be printed without space.

**Escape sequence** - \" ... \" to use quotation mark

# String Methods

name = name.strip() - removes all the whitespaces from the string
name = name.capitalize() - Capitalize only the first letter
name = name.title() - Title based Capitalization

**Chaining Methods**

name = name.strip().title()

first, last = name.split(" ") - split the string on the basis of a whitespace

if z = 1000, print(f"{z : ,}") - will output 1,000
if z = 0.666666666, print(f"{z : .2f}") - will output 0.67 - 2 floating point digits

# Defining Function

def Hello(name = "World"):
print(f"Hello, {name}")

name = input("Enter your name : ")
Hello(name)
Hello()

**A function must be defined before calling it**

To avoid this conflict :

def main():
name = input("Enter your name : ")
Hello(name)

def Hello(name):
print(f"Hello, {name}")

main()

# A function returning a value

def Name():
name = input("Enter your name : ")
return name

name = Name()
print(f"Hello, {name}")
