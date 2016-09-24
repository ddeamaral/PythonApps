#this is a display of Chapter 3 Lists of Python crash Course by Eric Matthes

# Important information from the book
# "what Is a list? A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, 
# the digits from 0–9, or the names of all the people in your family. You can put anything you want into a list, and 
# the items in your list don’t have to be related in any particular way. 
# Because a list usually contains more than one element, it’s a good idea to make the name of your list plural, such as letters, digits, or names"
#
#
#
#
#
#

bicycles = ['trek', 'cannondale', 'redline', 'specialized'] # you can hold multiple items in a list, strins, numbers and objects.
print(bicycles) # Python can print lists for you, but the output isn't so pretty
print(bicycles[0]) # you can access a list by a 0 based index like so. This prints out the first bicycle.
print(bicycles[0].title())# the output of bicycles[0] is a string, so you can use string methods on this element as shown by using .title()
print(bicycles[1]) # a position in the list is 0 based, meaning if you want the second item, you say bicycles[1] instead of bicycles[2]
print(bicycles[3]) # this is true for most programming languages

### Useful tip: if you have a list you don't know the index of, you can get the last index by asking for -1 ###
print(bicycles[-1]) # Python has a special syntax for asking for the last item in a list, by accessing the index of -1

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)


### Try it youself task 3-1 ###
#       3-1. Names: Store the names of a few of your friends in a list called names . Print each person’s
#   name by accessing each element in the list, one at a time .
friends = ['Sam', 'Mike', 'Brad', 'Alvaro', 'Blaise','Carlton'] # creatng a list of friends to print
# print out each friends name to practice list accessing
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
print(friends[-1])

message = "Hello " + friends[0].title()
print(message)

### Try it yourself 3-3
#   3-3 Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a 
#car, and make a list that stores several examples . 
#Use your list to print a series of statements about these 
#items, such as “I would like to own a Honda motorcycle .”

message = "My girlfriend's name is "  + friends[0].title() + "." #example of how to put list elements in a sentence
print message

message = "My friend " + friends[1].title() + " was in the USMC." #another example of putting an element in a sentence
print message

#### Changing, adding, and removing elements  #####
motorcycles = ['Honda', 'yamaha', 'suzuki'] #list of motorcycles to practice modifying lists
print motorcycles # just show what is in the list so far

my_motorcycle = 'Harley' #this is a variable that holds a string, which saves in memory
motorcycles[0] = my_motorcycle # reassigning the first element to the value of my_motorcycle to show how to overwrite a value

print(motorcycles) # showing the change
motorcycles.insert(0, my_motorcycle) #inject my motorcycle at index 0

print(motorcycles)# print results to show insert

del motorcycles[3] # if you know the position of your element, you can use the del keyword to delete it, this shows it

print(motorcycles)#reprint to show deletion of motorcycle

print(motorcycles[0].title())

