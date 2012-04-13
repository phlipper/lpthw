name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

# extra credit

# Change all the variables so there isn't the my_ in front. Make sure you
# change the name everywhere, not just where you used = to set them.

# Try more format characters. %r is a very useful one. It's like saying
# "print this no matter what".
print "print %r no matter what" % (1 + 2 + 3)

# Search online for all of the Python format characters.

# Try to write some variables that convert the inches and pounds to
# centimeters and kilos. Do not just type in the measurements. Work out the
# math in Python.
print "%d inches is the same as %.02f centimeters" % (5.0, (5.0 * 2.54))
print "%d pounds is the same as %.04f kilos" % (180.0, (180.0 * 0.4536))
