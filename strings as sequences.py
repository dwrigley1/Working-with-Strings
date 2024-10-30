'''
Python strings are sequences. Strings are not lists, but you can treat them like lists in many particular cases.
For example, if you want to access any of a string's characters, you can do it using indexing, just like in the example below. Run the program:
'''

# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

'''Be careful, don't try to pass a string's boundaries, it will cause an exception.'''

# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()