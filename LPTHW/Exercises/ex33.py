

def list_print(size, counter):
	numbers = []

	for i in range (0, size):
		print "At the top i is %d" % i
		numbers.append(i)

		print "Numbers now: ", numbers
		print "at the bottom i is %d" % i
		
#		i = i + counter

	print "The numbers: "

	for num in numbers:
		print num

print "Would you like me to make a list?"
print "Enter the size of the list:"
entries = int(raw_input())
print "You entered %r elements in the list" % entries

print "How would you like to increment this list?"
print "Enter value for increments:"
increment = int(raw_input())

list_print(entries, increment)
