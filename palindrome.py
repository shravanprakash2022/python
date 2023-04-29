
#1) Python program for palindrome number using iterative method
'''
n = int(input("provide number : "))
reverse,temp = 0,n
while temp!=0:
    reverse = reverse*10 + temp%10;        
    temp=temp//10;
if reverse==n:
    print("number is palindrome")
else:
    print("number is not palindrome")



#2)
def pal(num):
     n = num[::-1]
     if n == n:
       print('palindrome')
     else:
       print('not palindrome')
 print(pal('edureka'))


#3)
string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")


'''
#4) Python program for palindrome number using recursive method
n = int(input("please give a number : "))
def reverse(num):
    if num<10:
      return num 
    else:
      return int(str(num%10) + str(reverse(num//10)))
def isPalindrome(num):
    if num == reverse(num):
        return 1
    return 0
if isPalindrome(n) == 1:
    print("Given number is a palindrome")
else:
    print("Given number is a not palindrome")
#''' 
