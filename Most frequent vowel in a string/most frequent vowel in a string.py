s = input() #taking a string as input #helloworld
d = {
    'a': 0,"e": 0,"i": 0,"o": 0,"u": 0
}#initializing the occurence the vowels count to 0
for i in s:#h e l l o w o r l d
    if i in "aeiou":#h is not a vowel #e is in vowel
        print("The vowels in given string:",i)
        d[i] += 1 #e occured so e=1 # o occured 2 times
        print("The count of Vowel",i,":",d[i])
ans, maxValue = '',0 #initializing
for key, value in list(d.items()):#since we want to print it separately instead of tuples we are using key,value
    print(key,"-----",value)
    if value > maxValue:# here e=1 i.e; 1>0 #o=2 and 2>1
        ans = key #ans=e #ans=o 
        maxValue = value #maxvalue=1 #maxvalue=2
print("The most frequent vowel in the given string is:",ans)