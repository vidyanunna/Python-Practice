def targetsum(arr,target):
    index={}#empty dictionary to stores indices of elements in array
    compliment=0
    for i in range(len(arr)):
        compliment=target-arr[i]# Calculate the compliment of the current element.
        if compliment in index: # Check if the compliment is already in our dictionary.
            return[index[compliment],i] # If it is, return the indices of the two elements that add up to the target sum.
        index[arr[i]]=i # If not, add the current element and its index to the dictionary.
arr=list(map(int,input().split(" ")))
target=int(input())
print(targetsum(arr,target))