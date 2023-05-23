num1 = 25
num2 = float(num1)
print(type(num2))

num1 = 13.67
num2 = int(num1)
print(type(num2))

num1 = 5
num2 = 2
num3 = num1 // num2 #integer division
print(num3 == 5 % 3) #result is True

num1 = -11
num2 = abs(num1)
print(num2 == 11)

result = ((25 % 7 + 10 / 2) % 3 == 0) and ((abs(-19) / 2 - 2) > 9)
print(result) #should return False

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
print(my_list)  
my_list.pop(5)
my_list.append('C++')
my_list.remove(30)
index = my_list.index(10.5)
my_list.insert(4, 77)
my_list.extend([100, 101, 102])
howmany = my_list.count(20)

my_list = [10, 10.5, 20, 330, 50, 90, 111,1, 22]
print("hi")
asc = sorted(my_list)
print("sort", sorted(my_list))  

desc = sorted(my_list, reverse = True)
print("reverse sort", sorted(my_list, reverse= True))  

small = min(my_list)
print("min", min(my_list))  

large = max(my_list)
print("max", max(my_list))  

add = sum(my_list)
print("sum", sum(my_list))  
char = len(my_list)
print(char)
 
my_list.clear()
 
print("delete all elements", my_list)

my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
add = (my_list + [30.01, 30.02, 30.03]) * 2
print(add)


