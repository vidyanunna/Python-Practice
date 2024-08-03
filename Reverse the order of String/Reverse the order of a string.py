def reverseString(s):
    words=s.split() #splitting the words
    reverse_str=words[::-1] #reversing the word as a whole
    reverse=" ".join(reverse_str) 
    return reverse
s=input()
print(reverseString(s))