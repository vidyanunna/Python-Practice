n=int(input()) #10 #no.of votes
arr=list(map(int,input().split(" "))) # 1 1 1 1 1 2 2 3 3 3 so our ans should be 1
counter={}#Taking dictionary #to maintain count of individual election party
for i in arr:
    if i in counter: 
        counter[i]+=1 #if the vote is already present just increment the no.of votes
    else:
        counter[i]=1 #else just start counting with 1
print(*counter.items()) #prints key value pair
newArray=list(counter.items())#converts key value to list
print(newArray)
newArray.sort(key=lambda ele:ele[1]) #By using this syntax the tuples will be sorted based on the second value
#else if we use newarray.sort() then the tuples will be sorted based on first element
if newArray[-1][1]>newArray[-2][1]:# Check if the highest vote count is greater than the second highest vote count
    print(newArray[-1][0])
else:
    print(-1)#if no votes are higher that means no party won so print -1