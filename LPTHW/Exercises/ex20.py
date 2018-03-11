
#gets import modules
from sys import argv

#unpacks argv
script, input_file = argv

#define function to print file.  assigns f to whatever you pass into () later
def print_all(f):
	print f.read()

#seek lets you walk along position in file.  default is 0 (beginning)
def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)


