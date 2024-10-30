'''
The in & not in operators when applied to strings simply checks if its left argument (a string) can be found anywhere within the right argument (another string). 
The result of the check is True or False.
'''

# the in operator

alphabet = "abcdefghijklmnopqrstuvwxyz"

'''print("f" in alphabet) # True
print("F" in alphabet) # False
print("1" in alphabet) # False
print("ghi" in alphabet) # True
print("Xyz" in alphabet) # False'''

# the not in operator 

alphabet_two = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet_two) # False
print("F" not in alphabet_two) # True
print("1" not in alphabet_two) # True
print("ghi" not in alphabet_two) # False
print("Xyz" not in alphabet_two) # True