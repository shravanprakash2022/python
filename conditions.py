
x = "The days of Python 2 are almost over. Python 3 is the king now." 
if len(x) >= 50:
    print("True!")

if type(x) is str and x.startswith("T"):
    print("True!")

x = "The days of Python 2 are almost over. Python 3 is the king now."

if "wz" in x or x.count("zzz") >= 100:
    print("True!")
else:
    print("False")

if x.index("f") < 10:
    print("True!")
else:
    print("False")

#if x[-3:].isdigit():

#if len(x) >= 8 and type(x[6]) is float:

x = [115, 115.9, 116.01, ["length", "widt", "height"], 109, 115, 119.5, ["length", "width", "height"]]
 
if x[3][1].endswith("h") and x[7][0].endswith("h"):
    print("heheTrue!")
    print(x[3][0])
else:
    print("leleFalse!")


if x.count(115) >= 1 or x.index(115) == 0:
    print("Truell!")
else:
    print("False!")


 #if the largest key in the dictionary divided by the second largest key in the dictionary
 # returns a remainder equal to the smallest key in the dictionary. Otherwise, print out False!

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
 
if sorted(x.keys())[-1] % sorted(x.keys())[-2] == sorted(x.keys())[0]:
    print("Trueeee!")
else:
    print("False!")
