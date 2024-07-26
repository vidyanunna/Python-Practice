def solution(n,arr,num): #to find prime factorization # n:array length #arr: array #num=num to do prime factorization
    #since we are going for prime factorization it should be of form 16=2*2*2*2=2^4
    primes=[]
    if n==0:
        return -1 #if arr is empty return -1 as said
    while num%2==0:
        primes.append(2)
        num=num//2
    for i in range(3,(num**0.5)+1): 
        while num%i==0:
            primes.append(i)
            num=num//i
    if num>2:
        primes.append(num)
    print(primes)
    ans=0
    for i in primes:
        try:
            print("arr[i] is",arr[i])
            ans+=arr[i]
        except:
            return 0
    return ans
arr=list(map(int,input().split(" ")))
num=int(input())
ans=solution(n,arr,num)
print("answer is:",ans)