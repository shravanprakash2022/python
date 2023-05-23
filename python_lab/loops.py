x = [10, 12, 13, 14, 17, 19, 21, 22, 25]
for a in sorted(x, reverse = True):
    print(a*10)


for a in x:
    print(x.index(a))


x = 1
while x<=5:
    print("aaradhya get out ")
    print(x*x)
    x= x + 1



x = 0
while x<=4:
    print(x)
    x=x+1
else:
    print("Done")


#Write code that will iterate over the x and y lists and multiply each element of x with each element of y that is less than or equal to 10, also printing the results to the screen. 
#For y's elements that are greater than 10, multiply each element of x with y squared.

x = [2, 4, 6, 8]
y = [5, 10, 15, 20]
 
for i in x:
    for j in y:
        if j <= 10:
            print(i * j)
        else:
            print(i * j ** 2)


my_range = range(9)
 
for i in my_range:
    if 3 <= i <= 7:
        print("range",i * my_range[1])

x = [1, 2]
y = [10, 100]
 
for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)
            break
        print(i)
    print(j)