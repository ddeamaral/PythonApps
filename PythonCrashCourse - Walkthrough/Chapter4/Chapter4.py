#	Walkthrough of "Python Crash Course" by Eric Matthes
#	Iteration by Dylan DeAmaral
#	Chapter 4

######## Chapter 4 of walkthrough: Working wIth lists ########

# We created a list of magicians to loop through and demonstrate a loop to execute instructions on each element of the list
magicians = ['alive', 'david', 'carolina','penn', 'teller'] 

# This shows how to loop through
for magician in magicians:
	#print(magician) this was to simply display each magicians name
	# We are going to tell the magicians they performed a great trick
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")

# I already know how to use for loops, just getting the syntax out of the way
for  value in range(1, 6):
	print value

# When you use range, it simply produces a range of numbers. When you wrap range with list, it converts it to a list. Both range and list are enumerable.
even_numbers = list(range(2,11,2))
print even_numbers

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

# Demo of some simple statistical/mathematical functions
digits = range(0,10)
print min(digits)
print max(digits)
print sum(digits)

print digits

#####		List Comprehensions		#####


squares = [value**2 for value in range(1,11)]
print squares



####	Try it yourself		####

#		4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive .

for value in range(1,21):
	print value

# 		4-4. One Million: Make a list of the numbers from one to one million,
# and then use a for loop to print the numbers. 
# (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window .)

one_million_numbers = list(range(1,1000001))
# This loop took like 11 seconds to run. Commented out so I can build
# for number in one_million_numbers:
# 	print number


#	4-5. Summing a Million: 
#		Make a list of the numbers from one to one million, and then use min() and max() 
#		to make sure your list actually starts at one and ends at one million.
#		Also, use the sum() function to see how quickly Python can add a million numbers .


print( min( one_million_numbers ) ) 
print( max( one_million_numbers ) ) 
print( sum( one_million_numbers ) ) 

#	4-6. Odd Numbers: 
#		Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_numbers = list(range(1,21,2))
for number in odd_numbers:
	print number

#		4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

thirds = list(range(3,31,3))
for number in thirds:
	print number

#		4-8. Cubes: 
#	A number raised to the third power is called a cube. 
#	For example, the cube of 2 is written as 2**3 in Python. 
#	Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube


one_to_ten = list(range(1,11))
for number in one_to_ten:
	print number ** 3

#	4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cubes =  [value**3 for value in range(1,11)]
print cubes


#####		working with Part of a List 			#####

players = ['charles', 'martina', 'michael', 'florence', 'eli']

#	This is called slicing a list
# you can get a subset of a list of elements with this notation similar to accessing an index

print players[0:3]

print players[1:4]

#	If a beginning isn't specified, Python automatically grabs the beginning to the max of the specified range
print players[:4]


#	Similar to omitting a beginning, you can omit an end to your range and get the elements from your min to the end of the list as shown below
print players[ 2 :]

# This notation is helpful when you want to get the last three players in your list, you can use the negative number to retrieve the number of positions you specify off the end of the list as shown below

print players[-2:]

#	Note, these only work should the size of the players list is larger than the range of indexes you're trying to access/query

#	Slices are sill enumerable as they are just a subset of a list, which means they are still lists.

print "Here are the first three players on the team:"

for player in players[:3]:
	print player.title()


#####			Copying a list 				#####

#	You can copy a list by not specifying a min or max index. This simply copies the values and doesn't actually store a reference to the original list

my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]

# To prove we have two separate lists, we can add a new food to each list and keep track of the appropriate person's favorite food

#	Added these lines after showing that they are the same values, simply to test that they are separate lists and not referencing the same list
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:") 
print(my_foods)
print("\nMy friend's favorite foods are:") 
print(friend_foods)

#	This will actually make your foods be overwritten with friend_foods, and will also affect both if we append
my_foods = friend_foods

my_foods.append('cannoli')
print my_foods
print friend_foods

#	This is because we assigned the list that is stored in friend_foods is now what is stored in my_foods. my_foods actually points to the same list as friend_foods in memory, thus is the reason for canolli being added to both lists.


####			Try it yourself 				####

#	 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following
#	 Print the message The first three items in the list are Then use a slice to print the first three items from that programs list. 
#	 Print the message, Three items from the middle of the list are: Use a slice to print three items from the middle of the list. 
#	 Print the message, The last three items in the list are Use a slice to print the last three items in the list


print("The first three items in the list are: " + str(my_foods[:3]))
