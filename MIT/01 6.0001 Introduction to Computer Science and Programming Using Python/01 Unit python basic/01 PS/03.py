# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the
# letters occur in alphabetical order. For example,
# if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example,
# if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

# Note: This problem may be challenging. We encourage you to work
# smart. If you've spent more than a few hours on this problem, we
# suggest that you move on to a different part of the course.
# If you have time, come back to this problem after you've had a
# break and cleared your head.

# s = 'azcbobobegghakl'
# s = 'mxdiyhgaxbpbmxr'
# s = 'cuujolrhyjrnebaamzj'
s = 'abcdefghijklmnopqrstuvwxyz'
total = s[0]
total_prev = s[0]
for i in range(1, len(s)):
    if ord(s[i]) >= ord(total[-1]):
        total += s[i]
    else:
        total = s[i]
    if len(total_prev) < len(total):
        total_prev = total

print('Longest substring in alphabetical order is:', total_prev)
