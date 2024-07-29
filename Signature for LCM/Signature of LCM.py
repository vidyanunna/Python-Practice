#Calculating LCM and GCD
import math
def lcm(a,b):
    return a*b//math.gcd(a,b) #python has inbuilt fun to calculate gcd of a,b
a,b=list(map(int,input().split(" "))) #as we need to take input in a single line
print(math.gcd(a,b))
print(lcm(a,b))
