my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

number = len(my_tup)
print(number)
index = my_tup.index("Slovakia")
print(index)


my_tup = ("Romania", "Poland", "Estonia")
(ro, po, es) = my_tup
print(ro + ", " + po + ", " + es) #returns 'Romania, Poland, Estonia'

my_tup1 = ("Romania", "Poland", "Estonia","Estonia" "Bulgaria", "Slovakia", "Slovenia", "Hungary")
last = sorted(my_tup1)
print(last)
last = max(my_tup1)
print(last) #should return Slovenia

my_tup = ("Romania", "Poland", "Estonia","Estonia", "Bulgaria", "Slovakia","Estonia", "Slovenia", "Hungary")
number = my_tup.count("Estonia")
print(number)

