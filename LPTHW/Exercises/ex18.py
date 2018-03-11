#this one is like the scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#actually that *args is actually pointless-- just do this:
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no arguments
def print_none(arg1):
	print "I got nothin' %s " % arg1

print_two("Christine", "DaMean")
print_two_again("Christine", "DaMean")
print_one("FIRST")
print_none("...	!")
