n=int(input()) #ex:5
arr=list(map(int,input().split(" ")))#ex:1 2 3 4 5
arr.sort() # here in the example array is already sorted if not , sort the array
a,b=arr[-1],arr[-2] # here we are comparing from last num in arr that is larger num #so that the time complexity decreases
#ex:arr[1],arr[-2] is 5& 4
avg=(a+b)/2 #calculate the average between last 2 numbers #ex:avg =4.5
for i in range(n):
    if arr[i]<avg: #if any num which are less than the average  #ex: except 5 everything is less than 4.5
        arr[i]=0 #update it to 0 #ex: so update everything to 0
print(sum(arr)) #update the total sum #print the sum of remaining numbers which is 5 :)
    

