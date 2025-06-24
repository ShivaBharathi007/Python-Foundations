# Basic Slicing Syntax
# string[start:stop:step]

s = "abcdefghij"
# Index:      0  1  2  3  4  5  6  7  8  9
#             a  b  c  d  e  f  g  h  i  j
# Negative: -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# 1. Get last N characters
print(s[-3:])       # 'hij'   → last 3 characters
print(s[-1:])       # 'j'     → last character
print(s[-5:])       # 'fghij' → last 5 characters

# 2. Remove last N characters
print(s[:-1])       # 'abcdefghi' → all except last 1
print(s[:-3])       # 'abcdefg'   → all except last 3
print(s[:-9])       # 'a'         → all except last 9

# 3. Middle slice using negative indices
print(s[-7:-2])     # 'defgh' → from index -7 to -3
print(s[-6:-3])     # 'efg'   → from index -6 to -4

# 4. Reversed full string
print(s[::-1])      # 'jihgfedcba' → full reverse

# 5. Reversed slices
print(s[-2:-7:-1])  # 'ihgfe' → backward from -2 to -7 (exclusive)
print(s[-1::-1])    # 'jihgfedcba' → full reverse (explicit)
print(s[-4::-2])    # 'geca' → reverse from -4 every 2nd char

# 6. Last N characters in reverse
print(s[:-6:-1])    # 'jihgf' → reverse last 5 characters
print(s[-1:-6:-1])  # 'jihgf' → same as above, explicit start

# 7. Skip in reverse
print(s[::-2])      # 'jhfdb' → every 2nd character in reverse
print(s[-2::-2])    # 'igeca' → from -2 to start, every 2nd char
print(s[-1:-10:-3]) # 'jgc'   → from end to start, step -3
