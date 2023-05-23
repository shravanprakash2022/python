i,temp=0,0
n = int(input("please give a number : "))
for i in range(2,n//2):
    if n%i == 0:
        temp=1
        break
if temp == 1:
    print("given number is not prime")
else:
    print("given number is prime") 


'''
#2) prime number

n = int(input("please give a number : "))
for i in range(2, n//2):
 if n%i == 0:
  print ("number is not prime")
  break
 else:
  print(" number is prime")


#3)prime using functions
import math
def is_prime(n):
  if n < 2:
     #print("not prime")
     return False
  for i in range(2, int(math.sqrt(n)) + 1):
      if n % i == 0:
      #   print("not prime")
         return False
  #print("prime")
  return True
n = 4
print(is_prime(n))
'''
