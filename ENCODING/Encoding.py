n=input()#167 - then o/p should be 1^2 6^2 7^7 - 13649
res=""
for i in n:
    cur_num=int(i) #converting string to integer
    res+=str(cur_num**2) #square the num and convert to string and add to the res
print(res)