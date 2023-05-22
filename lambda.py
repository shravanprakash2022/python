

def sq(num):
    result = num**2
    return result
my_nums= [1,2,3,4,5,6,7]

#################
sq = lambda num: num**2
print(sq(5))
#print(sq(5))   

#################
#map functions
#for item in map(sq, my_nums):
  #  print(item)

#my_nums= [1,2,3,4,5,6,7]
names= ['shravan', 'aaradhya', 'sahithya', 'kavitha']
#same above with lambda
print(list(map(lambda num: num**2, my_nums)))
print(list(map(lambda num: num%2 ==0, my_nums)))
print(list(filter(lambda num: num%2 ==0, my_nums)))
print(list(map(lambda num: num[1:3], names)))
