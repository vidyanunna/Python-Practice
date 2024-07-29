# #i/p - 
# 5
# 2 4 7 3 3 
# o/p:
# 3 - which is index number of 7
def equilibrium(n,arr): #n=length of arr #arr=array
    target_sum=sum(arr) #target_sum = sum of elements in array # target_sum=2+4+7+3+3 =19
    left=0 
    for i in range(1,n+1): #As told indexing should be start from "1" 
        right=target_sum-left-arr[i-1] #1 : right=19-0-arr[0]==> right=19-0-2==>17
         #2: r=19-2-arr[1]==> r=19-2-4==>13
         #3: r=19-6-arr[2]==>r=19-6-7==>6
        if left==right: #3 iteration :6==6
            return i #3 iteration :3
        else: #if left !=right
            left+=arr[i-1] #left=0+2==>2 #2: 2+4=6
    return "NOT FOUND"
n=int(input())
arr=list(map(int,input().split(" ")))
print(equilibrium(n,arr))