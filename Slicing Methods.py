# Basic Slicing Syntax
# string[start:stop:step]



text = 'engineering'

# # 1. Basic Forward Slicing
# print(text[0:4])      # 'engi' → from index 0 to 3

# 2. Omitting start or stop
# print(text[:6])        # 'engine' → from beginning to index 5
# print(text[0:])        # 'ineering' → from index 3 to end
#
# # 3. Negative Indexing
# print(text[-3:])       # 'ing' → last 3 characters
# print(text[:-4])       # 'enginee' → all except last 4 characters
#
# # 4. Full Copy of the String
# print(text[:])         # 'engineering' → entire string



# # 5. Slicing with Step
# print(text[::2])       # 'egnenn' → every 2nd character
# print(text[1::3])      # 'neng' → from index 1, every 3rd character
#
# # 6. Reverse String
# print(text[::-1])      # 'gnireenigne' → reverse the string


### Index:      0  1  2  3  4  5  6  7  8  9  10
#             e  n  g  i  n  e  e  r  i  n   g
# Negative: -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# # 7. Substring from End Towards Start
# print(text[-1:-5:-1])  # 'gnir' → last to 4th-from-end (exclusive)
#
# # Practical Slicing Use Cases
#
# # Extracting File Extensions
filename = 'report.pdf'
print(filename[-3:])   # 'pdf' → last 3 characters




