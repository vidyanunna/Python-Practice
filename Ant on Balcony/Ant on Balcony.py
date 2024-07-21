n=int(input())#no. of moves made by ant
arr=list(map(int,input().split(" ")))# arr consistting of ant moves
# 1 means moving towards right "-1" means moving towards left
#arr=[1,-1,1,-1,1]
count=0 #how many times ant reached the origin
total=0
for i in arr:#1#-1
    total+=i#total=1#total=1-1=0
    print("Move made by the Ant:", total)
    if total==0:#1!=0 go to for loop #0=0i.e met origin
        count+=1#1st time ant met origin
print("How many times ant reached the origin:",count)#total count of ant meeting origin