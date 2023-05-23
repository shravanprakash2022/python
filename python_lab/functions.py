def my_func(x,y,z):
    return x ** y + z
 
result = my_func(3,3,3)
print(result)



def my_func(x, *args):
    return x * args[1]
 
result = my_func(5, 10, 20, 30, 50)
print(result)


def my_func(x, **kwargs):
    return x * sorted(kwargs.values())[-1]
 
result = my_func(10, val1 = 10, val2 = 15, val3 = 20, val4 = 25, val5 = 30)
print(result)


var = 10

def my_func(x):
	print( x*var)
	
my_func(20) 