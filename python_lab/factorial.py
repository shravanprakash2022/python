'''def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
#num = 5 
num = int(input("Enter "))
print( num, "is/n", factorial(num))
'''

def fact(n):
 if n <= 0:
  return 1
 else :
  return n * fact(n-1)
print(fact(3))


