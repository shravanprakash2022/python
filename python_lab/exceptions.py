x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)


try:
    print(25 % 0)
except ZeroDivisionError:
    print("zero!")

try:
    print(25 % 5 ** 5 + 5)
except:
    print("Bug!")
else:
    print("Clean!")



try:
    print(25 % 0 ** 5 + 5)
except:
    print("Bug!")
finally:
    print("Result!")


x = [1, 9, 17, 32]

try:
    print(x[3] % 3 ** 5 + x[4])
except ZeroDivisionError:
    print("Zero!")
except IndexError:
    print("Index!")


try:
    print(25 % 5 ** 5 + 5)
except ZeroDivisionError:
    print("Zero!")
else:
    print("Clean!")
finally:
    print("Finish!")