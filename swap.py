'''
#1)Python program to swap two number without using third variable
a = int(input("please give first number a: "))
b = int(input("please give second number b: "))
a=a-b
b=a+b
a=b-a
print("After swapping")
print("value of a is : ", a);
print("value of b is : ", b);
'''


#2)

a,b=2,5
print("Before swap \na =",a, "\nb =",b)
a,b=b,a
 
print("after swap \na =",a, "\nb =",b)
