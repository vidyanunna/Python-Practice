def isprime(num): #checking if number is prime or not
    if num in (0,1):  #if the number is in 0 or 1
        return False # returns false since 0&1 are not prime numbers
    else:
        for i in range(2,int(num**0.5)+1): #else it checks from 2 to square root of number
             #here the next num of 6 is 7 so in range of (2,int(square root of 7)+1)==> (2,int(2.645)+1)==>
             #  since it is in int it takes only integer value ==> (2,2+1)==> so it checks from range(2,3)
            if num%i==0: # if the num is divisible by 2/3 then it is prime num
                return False #return false
        return True #else it is prime number and prints the number :)
num=int(input())#6
nextNum=num+1 #7 #Execution starts here
while True: #if the nextnum is prime
    if isprime(nextNum): 
        print(nextNum)#it prints the next number
        break
    nextNum+=1 # else it increments and check if the num is prime or not