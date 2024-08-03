# Problem Statement:
# Pangram is a sentence containing every letter in the English alphabet. Given a string, find all characters that are missing from the string, Le., the characters that can make the string a Pangram We need to print output in alphabetic order.
# For example,
# Input: welcome to geeksforgeeks
# Output: abdhijnpquvxyz
def missing(s):
    d="" #initializing an empty string to store missing elements
    s=s.lower() #converting all strings to lower case
    alphabets="abcdefghijklmnopqrstuvwxyz"
    for i in alphabets: # if i in alphabets
        if i not in s: #and not in s
            d+=i #add the character to the string
    return d
s=input()
print(missing(s))