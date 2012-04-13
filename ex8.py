formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)


# Extra Credit

# Do your checks of your work, write down your mistakes, try not to make them
# on the next exercise.


# Notice that the last line of output uses both single and double quotes for
# individual pieces. Why do you think that is?

# ^^ The output changes because of the single quote in the word `didn't`
