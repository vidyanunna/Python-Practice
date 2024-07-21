n=int(input()) #no.of problems to solve in a contest # 6
p=int(input())#time required to reach the contest venue in minutes i.e 4 hours 4*60=240
time_remaining=240-p#time remaining to solve problems 
#p=180 min i.e 240-180 =60 min How many problems can be solved?
count=0
for i in range(1,n+1):#from 1 to 6
    solve_time=i*5# each problem requires 5*i i.e; 1prob-5*1 2 prob -5*2 and so on
    if solve_time<time_remaining and time_remaining>0:
        count+=1
        print("question solved:",count)
        time_remaining-=solve_time
print(count)