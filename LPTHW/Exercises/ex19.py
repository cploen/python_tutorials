def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
#line below not working yet
#	print "That means you have" boxes_of_crackers*60 "actual crackers"
	print "Man, that's enough for a party!"
	print "Get a blanket.\n"

#LifeGoals how do I put cracker counter inside previous function so I can inherit the number of boxes?
def cracker_counter(boxes, crackers_per_box):
	print "Each box has %d crackers per box." % crackers_per_box
	total_crackers = boxes * crackers_per_box
	print "That means you have %d crackers" % total_crackers

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "test the cracker counter"
cracker_counter(amount_of_crackers, 60)

