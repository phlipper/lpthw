tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


# Extra Credit

# Search online to see what other escape sequences are available.

# Use ''' (triple-single-quote) instead. Can you see why you might use that
# instead of """?
skinny_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print skinny_cat

# ^^ In this example, the output is the same. More research is required.

# Combine escape sequences and format strings to create a more complex format.
# Remember the %r format? Combine %r with double-quote and single-quote
# escapes and print them out. Compare %r with %s. Notice how %r prints it the
# way you'd write it in your file, but %s prints it the way you'd like to see
# it?
format = """
"%r" '%r' %s
"""
print format % ("foo", "bar", "baz")