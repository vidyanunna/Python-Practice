def triplets(n,arr,prod): #n:length of array #arr=array#prod=product 
    if len(arr)==0:
        return -1
    count=0
    arr.sort() 
    for i in range(n-2): # we are using n-2 because we need atleast three elements to form a triplet
        left=i+1 # after i
        right=n-1 #right starts from last element
        while left<right:
            triplets=arr[i]*arr[left]*arr[right]
            if triplets==prod:
                count+=1
                left+=1
                right-=1
            elif triplets<prod:
                left+=1
            else:
                right-=1
    return count
n=int(input())
arr=list(map(int,input().split(" ")))
prod=int(input())
print(triplets(n,arr,prod))