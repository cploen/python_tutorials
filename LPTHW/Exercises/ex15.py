#this is an import, adding features (really, "modules")  to the script.  
#argv holds the arguments passed to the script in the command line.
from sys import argv

#this line unpacks argv
script, filename = argv

#takes a parameter and passes value to my variable "txt".  This opens the file.
txt = open(filename)

#prints filename which was captured at command line
#then uses read command on txt with dot operator.
print "Here's your file %r:" % filename
print txt.read()

txt.close()

#prompts user for new filename to do this again
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
