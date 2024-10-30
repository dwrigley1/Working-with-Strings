'''
Slicing is the extraction of a part of a string, list, or tuple. 
It enables users to access the specific range of elements by mentioning their indices. 
Syntax: Object [start:stop:step] “Start” specifies the starting index of a slice. “Stop” specifies the ending element of a slice.
'''

# Slices

alpha = "abdefg"

print(alpha[1:3]) # output -> bd
print(alpha[3:]) # output -> efg
print(alpha[:3]) # output -> abd
print(alpha[3:-2]) # output -> e
print(alpha[-3:4]) # output -> e 
print(alpha[::2]) # output -> adf
print(alpha[1::2]) # output -> beg
