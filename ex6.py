# setup the joke
x = "There are %d types of people." % 10

# add some details
binary = "binary"
do_not = "don't"

# the punch line
y = "Those who know %s and those who %s." % (binary, do_not)

# print the setup and punch line
print x
print y

# repeat the setup and punch line
print "I said: %r." % x
print "I also said: '%s'." % y

# describe the joke
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# tell the truth
print joke_evaluation % hilarious

# another string concatentation example
w = "This is the left side of..."
e = "a string with a right side."

# print the strings
print w + e


# Extra Credit

# Go through this program and write a comment above each line explaining it.

# Find all the places where a string is put inside a string. There are four
# places.

# Are you sure there's only four places? How do you know? Maybe I like lying.

# ^^ There are 4: line 1 and line 13 are not interpolating string values

# Explain why adding the two strings w and e with + makes a longer string.

# ^^ When the `+` is used on a string, it means concatenation vs. integer
# addition