from sys import argv
#from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line, too.
in_file = open(from_file).read()

#uses data formatter and command len which returns length of argument
#print "The input file is %d bytes long" % len(indata)

#returns whether file exists (T/F)
#print "Does the output file exist? %r" % exists(to_file)

#print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#write one file to another
out_file = open(to_file, 'w').write(in_file)


#print "alright, all done."

#close files
#out_file.close()
#in_file.close()
