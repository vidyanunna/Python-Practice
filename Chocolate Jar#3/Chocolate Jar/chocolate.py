n=int(input()) #3
arr=list(map(int,input().split(" ")))#10 20 30: no of chocolates in jars
total_choco_for_a=0
for box in arr:#since we have 3 jars we are using loop
    total_choco_for_a+=box//3#since we have 3 mem to distribute chocos i.e A,B,C we are dividing with 3
    #since we want that in int values and not in decimal values we are using "//"
    print(total_choco_for_a)
    if box%3!=0:# After distributing equally between A,B,C if we are having extra chocolates then again redistribute
        total_choco_for_a+=1#This will add up all the chocolates A got from all the three jars
print(total_choco_for_a)#returns total chocos for A