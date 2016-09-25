#Workthrough the book of Python Crash Course Chapter 2 By Eric Matthes

############### String Variables ##########################

# Condensed information from the book on 'naming and using vairables'
# You should follow some rules when naming your variables in Python
# 1) Variable names can only contain numbers, letters and underscores, and can only start with a letter or number
# For Exmaple: myVariable (good) _myVariable(good) 2myVariable (won't compile)
# 2) You can't have spaves in variable names like most programming languages. Typically, a underscore would be used in place of a space.
# 3) Avoid using Python keywords for variables that Python uses to function such as the word print
# 4) Advice: you should have descriptive and short variable names
# Example: Name is better than n, student_name is better than s_n, name_length is better than length_of_persons_name


message = "Hello Python world!" #assigning a message to the variable 'message' so later it can be printed to the console
print(message)

message = "Hello Python crash Course World!" # we re assigned the value of the 'message' variable and reprinted so it would have a different message printed
print(message) 


############### Numeric Variables ##########################

### Integers ###
Sum = 2 + 3  #display of how to add
difference = 3 - 2 #display of how to subtract
product = 2 * 3 #display of how to multiply
quotient = 3/2 #display of how to divide

ThreeSquared = 3**2 # how to square a number
ThreeCubed = 3**3 # how to cube a number
ToTheSixth = 10**6 #example of how to raise to any exponent


### Order of Operations ###
ExpressionResult = 2 + 3 * 4 # note the order of operations is supported in python
ExpressionResult2 = (2 + 3) * 4 # further demoing order of operations


### Floats ###

#Important note : Python declares any number with a decimal point a float (a number that can have a decimal point in any position)

FloatAddition = 0.1 + 0.1
FloatAddition2 = 0.2 + 0.2
FloatMultiply = 2 * 0.1
FloatMultiply2 = 2 * .02

#Beware that Python like most other languages has to store numbers to be as precise as possible due to the way numbers are stored
print(0.2 + 0.1)
print(3 * 0.1)
print(Sum)
#Avoid type errors with the str() function
age = 23
message = "Happy " + str( age ) + "rd Birthday!"
#print(message) # if uncommented, will throw an error: Can't convert 'int' object to str implicitly 

#Note, in python 2, division of numbers is different. 3 / 2 in python 2 results in 1 instead of 1.5
#To avoid this, make sure at least one of your number in your expression has a decimal point

#################### Very important information about commenting ##########################
# What Kind of Comments Should You Write? The main reason to write 
# comments is to explain what your code is supposed to do and how
# you are making it work. When you’re in the middle of working on a project, 
# you understand how all of the pieces fit together. But when you return to a project
# after some time away, you’ll likely have forgotten some of the details. You can always
# study your code for a while and figure out how segments were supposed to work, 
# but writing good comments can save you time by summarizing your overall approach 
# in clear English. If you want to become a professional programmer or collaborate
# with other programmers, you should write meaningful comments. 
# Today, most software is written collaboratively, whether by a group of employees 
# at one company or a group of people working together on an open source project. 
# Skilled programmers expect to see comments in code, so it’s best to start adding
# descriptive comments to your programs now. Writing clear, concise comments in your code is
# one of the most beneficial habits you can form as a new programmer. When you’re determining
# whether to write a comment, ask yourself if you had to consider several approaches before
# coming up with a reasonable way to make something work; if so, write a comment about your
# solution. It’s much easier to delete extra comments later on than it is to go back and
# write comments for a sparsely commented program. From now on, I’ll use comments in examples
# throughout this book to help explain sections of code.

import this # This will output the basic rules of Python that you should try to follow.
