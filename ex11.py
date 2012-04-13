print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)



# Extra Credit

# Go online and find out what Python's raw_input does.
# ^^ http://docs.python.org/library/functions.html#raw_input

# Can you find other ways to use it? Try some of the samples you find.
echo = raw_input("[echo] -> ")
print "ECHO: %s" % echo

# Write another "form" like this to ask some other questions.
print "Do you like this book so far? ",
answer1 = raw_input("(yes/no) ")
print "Are we having fun yet? ",
answer2 = raw_input("(yes/no) ")
print "You answered %r to liking this book and %r to having fun" % (
    answer1, answer2)

# Related to escape sequences, try to find out why the last line has '6\'2"'
# with that \' sequence. See how the single-quote needs to be escaped because
# otherwise it would end the string?
