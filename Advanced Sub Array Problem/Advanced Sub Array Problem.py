n=int(input())#5
k=int(input())#3
arr=list(map(int,input().split(" "))) #9 2 5 3 7
ans=0#max score
for i in range(0,n-k+1):#since we are taking 3 elements in a sub array we have gone for +1
     #initillay it takes arr[0,1,2] i.e [9,2,5] then [2,5,3] then [5,3,7]
    sub_arr=arr[i:i+k]#slicing array i.e (0,0+3) from 9 to 5
    print(sub_arr)#takes sub array from full array p.s the sub array should be contigous
    sum=0 
    for ind in range(1,k+1):
        sum+=sub_arr[ind-1]*ind #ex:9*1+2*2+5*3=28
    if sum>ans:#since the problem is to find max score 
        ans=sum
print(ans)#prints max score from all sub arrays