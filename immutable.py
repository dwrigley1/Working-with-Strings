'''
Python's strings are immutable.
This primarily means that the similarity of strings and lists is limited. Not everything you can do with a list may be done with a string.
The first important difference doesn't allow you to use the del instruction to remove anything from a string.
The example here won't work:
'''

alphabet = "abcdefghijklmnopqrstuvwxyz"
del alphabet[0] # Traceback error

# The only thing you can do with del and a string is to remove the string as a whole

'''
Python strings don't have the append() method, you cannot expand them in any way.
The example below is erroneous:
'''

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.append("A") # Attribute error

'''
with the absence of the append() method, the insert() method is illegal, too
'''

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.insert(0, "A") # Attribute error

'''
Don't think that a string's immutability limits your ability to operate with strings.
The only consequence is that you have to remember about it, and implement your code in a slightly different way, look at the example code in the editor.
'''

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet) # output -> abcdefghijklmnopqrstuvwxyz