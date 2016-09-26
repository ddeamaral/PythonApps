#	Walkthrough of "Python Crash Course" by Eric Matthes
#	Iteration by Dylan DeAmaral
#	Chapter 3

# Important information from the book
# "what Is a list? A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, 
# the digits from 0–9, or the names of all the people in your family. You can put anything you want into a list, and 
# the items in your list don’t have to be related in any particular way. 
# Because a list usually contains more than one element, it’s a good idea to make the name of your list plural, such as letters, digits, or names"

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

print(motorcycles)
last_owned = motorcycles.pop() #use pop to get the last item in the list and store it in a variable for use later
print "pop removed the last item and stored it in last_owned"
print("The last motorcycle that I owned was a " + last_owned.title() + ".")
print(motorcycles)

print "you can take values out of lists by value with list.remove('value')"
motorcycles.remove('Harley') # this function removes the first instance of the value passed to the function. This does not remove all items with that value
print str(motorcycles) + ' notice the first harley was removed'

##### Try it yourself exercises #####
####	Exercise 3-4	###
# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, 
# who would you invite? Make a list that includes at least three people you’d 
# like to invite to dinner . Then use your list to print a message to each 
# person, inviting them to dinner.

guest_list = ['Franklin Delano Roosevelt', 'Thomas Edison', 'Mahatma Ghandi']

print "Greetings Former President " + guest_list[0] + ', I would like to invite you to a classic italian dinner.'

print "Hello Mr. " + guest_list[1].title() + ", I would like to invite you to dinner and discuss some of your inventions and discoveries."

print "Hi there Mr. " + guest_list[-1].title() + ". I would like to eat some chinese food and understand more of your philosophical standpoints."

####	Exercise 3-5	####
#3-5. Changing Guest List: You just heard that one of your guests can’t make 
# 			the dinner, so you need to send out a new set of invitations . You’ll have to
#			think of someone else to invite . Start with your program from Exercise 3-4
#			Add a print statement at the end of your program stating the name of the 
# 			guest who can’t make it . Modify your list, replacing the name of the 
# 			guest who can’t make it with the name of the new person you are inviting . 
#			Print a second set of invitation messages, one for each person who is still in your list . 


cancelled_guest = guest_list.pop()
# guest_list.remove(cancelled_guest)
guest_list.append('Stephen Colbert')


print "Greetings Former President " + guest_list[0] + ', I would like to invite you to a classic italian dinner.'

print "Hello Mr. " + guest_list[1].title() + ", I would like to invite you to dinner and discuss some of your inventions and discoveries."

print "Hi there Mr. " + guest_list[-1].title() + ". I would like to have some Ben and Jerrys with you and talk about modern society."

#		3-6. More Guests: You just found a bigger dinner table, 
# so now more space is available . Think of three more guests to invite to  dinner.
# Start with your program from Exercise 3-4 or Exercise 3-5 . 
# Add a print statement to the end of your program informing people that you found a bigger dinner table . 
#	Use insert() to add one new guest to the beginning of your list . 
#	Use insert() to add one new guest to the middle of your list . 
#	Use append() to add one new guest to the end of your list . 
#	Print a new set of invitation messages, one for each person in your list .

print "Good news! we found a bigger table and have room for more guests"

guest_list.insert(0, 'Jennifer Anniston')
guest_list.insert(len(guest_list) / 2, "Mark Wahlberg")
guest_list.append('Guido van Rossum')

print "Hey " + guest_list[0] + ", you are invited to dinner to eat with some of the greatest people."

print "Hey " + guest_list[1] + ", you are invited to dinner to eat with some of the stars."

print "Hey " + guest_list[2] + ", you are invited to dinner to eat with some of the stars."

print "Hey " + guest_list[3] + ", you are invited to dinner to eat with some of the stars."


print "Hey " + guest_list[4] + ", you are invited to dinner to eat with some of the stars."
print "Hey " + guest_list[5] + ", you are invited to dinner to eat with some of the stars."

print "Oops, we only currently have two seats available for dinner now"

####	3-7. Shrinking Guest List:	####
#	You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests . 
#	•	Start with your program from Exercise 3-6 . 
#		Add a new line that prints a message saying that you can invite only two people for dinner . 
#	•	Use pop() to remove guests from your list one at a time until only two names remain in your list . Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner . 
#	•	Print a message to each of the two people still on your list, letting them know they’re still invited . 
#	•	Use del to remove the last two names from your list, so you have an empty list . Print your list to make sure you actually have an empty list at the end of your program

cancelled_guest = guest_list.pop()
print "Sorry, we ran out of seats at the last minute Mr. " + cancelled_guest
cancelled_guest = guest_list.pop()
print "I'm so sorry, we lost the last couple of seats needed to seat everyone. I hope we can reschedule for another time Mr. " + cancelled_guest
cancelled_guest = guest_list.pop()
print "I'm so sorry, we lost the last couple of seats needed to seat everyone. I hope we can reschedule for another time Mr. " + cancelled_guest
cancelled_guest = guest_list.pop()
print "I'm so sorry, we lost the last couple of seats needed to seat everyone. I hope we can reschedule for another time Mr. " + cancelled_guest
del guest_list[-1]
del guest_list[-1]
print guest_list

####		Sorting		####

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # this methods use is simply to display you can auto sort lists and it is irreversible
print cars
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print cars
#notice that the sort method actually affects the cars list. The following is simply an example to display that list sorted without editing the list itself

print("Here is the original list:") 
print(cars)
print("\nHere is the sorted list:") 
print(sorted(cars))
print("\nHere is the original list again:") 
print(cars)

#important note about sorted(list), you can still pass the named parameter reverse=True like so

print sorted(cars, reverse=True)

print "length of the cars list is " + str(len(cars))