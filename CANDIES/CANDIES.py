N,K,A=list(map(int,input().split(" "))) #N - no of students #K- No.of chocolates # A- from where u start distribute chocos
ans=(A+K-1)%N #formula to find out who gets the last choco
if ans==0: #if ans=0 then all got the chocos
    print(N) 
else:
    print(ans) #student who got the final chocolate
# example:
# 4 students 5 chocos and start from "2" Person 

# 1     2      3      4     
#      choc1  cho2   cho3  
# cho4 cho5=end=ans