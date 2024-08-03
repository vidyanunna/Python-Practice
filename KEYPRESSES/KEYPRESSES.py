#In this program u should take "00" as one keypress
# so if u take 800 there should be 2 key presses 8-1 and 00-1 total of 2
num=input() 
count=0 #initialize the keypress counts
i=0
n=len(num)
while i<n:
    if i<n-1 and num[i]=='0' and num[i+1]=='0': 
        #so if adj places are 0 increment the count of keypresses
        count+=1
        i+=2 #so here u are already comparing 2 pos so increment 2
    else: #if there are no adj 0 congo :) just increment by 1
        count+=1
        i+=1
print(count)