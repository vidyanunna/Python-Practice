s=input()#aaabbbccdddd #magic string is converting all the alphabets in string to same alphabets 
# since here the count of d is more than a,b,c so all the alphabets should be converted to "d"
d={} #dictionary
for i in s:
    if i in d.keys(): 
        d[i]+=1 #if key is already present in d just increment
    else:
        d[i]=1#else start counting
ans=len(s)-max(d.values())# since here the count of d is more than a,b,c so total length-length of d will give u the required ans
print(ans)#8