# #input:
# 1 -2 3 4
# o/p:
# 6
arr=list(map(int,input().split(" ")))
total=0 
curr=-1
for i in arr:
    total+=i #1 #1-2=-1 #-1+3=2 #2+4=6
    print("total:",total)
    curr=max(curr,abs(total)) #(-1,1) #(1,1) #(1,2) #(2,6)
    print("tem curr",curr) #1 #1 #2 #6
print(curr)