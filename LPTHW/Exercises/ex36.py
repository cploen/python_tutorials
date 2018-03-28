from sys import exit

def great_pyramids():
	# do stuff
	dead("Congratulations.  Your body will be preserved for eternity alongside unfathomable riches!")

def rainforest():
	print """
	That was a risky choice!
	Luckily, zombie goldfish only crave fish blood, and you swim to shore unscathed.
	You notice the most heavenly aroma emanating from a nearby village.
	However, to get there, you must either wade through a fire swamp or climb through the canopy.
	Which do you choose?
	"""
	
 	next = raw_input("> ")
	
	if next == "wade":
		dead("You have perished in a fire swamp and your body has been consumed by thousands of ants.")

	elif next == "climb":
		print "Wowee!  You're more ambitious than you look!  Your upper body strength pays off here, "
		print "but a vine snaps and you land smack dab in the center of the tribal bakery"
		bakery()

	else:
		dead("You were frozen in fear and died as a tiger devoured your motionless body")
def bakery():
	# do stuff
	dead("That was one too many cupcakes for you!  Death by glucose overload.")

def success():
	# do stuff
	dead("You retire early and enjoy a life of leisure and competency in all that you attempt.")

def dead(why):
	print why
	exit(0)

def start():
	print "You wake up alone in a leaking canoe floating down a river."
	print "There are zombie goldfish swarming the boat."
	print "Do you row or swim?"
	
	next = raw_input("> ")

	if next == "row":
		great_pyramids()
	elif next == "swim":
		rainforest()
	else:
		dead("That was the worst possible option.  You're definitely dead now.")

start()

