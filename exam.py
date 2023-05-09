'''
import string, os, sys
def count_words(filepath):
    with open("/Users/shravannidankavi/Downloads/word.txt", 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)
 
print(count_words("words1.txt"))
print(count_words("/Users/shravannidankavi/Downloads/word.txt"))


with open("/Users/shravannidankavi/Downloads/word.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")


import math
print(math.sqrt(9))

import math
print(math.cos(1))

import math
print(math.pow(3,3))

 
'''
'''
a = [1, 2, 3]
b = (4, 5, 6)

for i,j in zip(a,b):
    print(i+j)

import string, os, requests
with open("/Users/shravannidankavi/Downloads/word.txt", "w") as file:
    for i,j,k in zip(string.ascii_lowercase[0::3], string.ascii_lowercase[1::3], string.ascii_lowercase[2::3]):
     print(i,j,k)
     file.write(i+j+k+"\n")
''''''

#for i in string.ascii_lowercase:
 #   with open("/Users/shravannidankavi/Downloads/"+ i + ".txt", "w") as file:
  #   print(i)
   #  file.write(i+"\n")


import glob
letters = []
file_list = glob.iglob("/Users/shravannidankavi/Downloads/*.txt")
check = "python"
for filename in file_list:
    with open(filename,"r") as file:
        letter = file.read().strip("\n")
    if letter in check:
        letters.append(letter)
 
print(letters)


for letter in "Hello":
    if letter == "e":
     print(letter)



#age = input("What's your age? ")
#age_last_year = int(age) - 1
#print("Last year you were %s." % age_last_year)


print(type("Hey".replace("ey","i")[-1]))


#firstname = input("Enter first name: ")
#secondname = input("Enter second name: ")
#print(f"Your first name is {firstname} and your second name is{secondname}")

import json
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}


#print(d["employees"][2]['lastName'])
d["employees"][1]['lastName'] = "smooth"
print(d)

d["employees"].append(dict(firstName ="Shravan", lastName="Nidankavi"))
print(d)

with open("company1.json", "w") as file:
    json.dump(d, file, indent=3)


import json
from pprint import pprint
 
with open("company1.json","r+") as file:
    d = json.loads(file.read())
pprint(d)

a = [1, 2, 3] 
for index,i in enumerate(a) :
   print(index,i)
   
#import time

#while True:
 #  i =i+1
  # print("get outta here.. aaradhya\n")
  # time.sleep(i)
  # if i == 3:
  #  break
  #  print("Sahithya")

#translator, try exception
#d = dict(weather = "clima", earth = "terra", shravan = "nidankavi", rain = "chuva")
##def vocabulary(word):
  ##   return d[word]
   # except KeyError:
   #    return "word doesnt exists"
#word = input("Enter word: ").lower()
#print(vocabulary(word))

'''
'''
import requests
headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("http://www.pythonhow.com", headers = headers)
print(r.text[:100])
'''
'''
import requests
response = requests.get("http://www.google.com", headers = {'user-agent': 'customUserAgent'})
text = response.text
print(text)
'''
'''
import requests
 
response = requests.get("http://www.pythonhow.com/data/universe.txt")
text = response.text
count_a = text.count("a")
print(count_a)
'''


#Google searcher
import webbrowser
#query =(input("enter your search:"))
#webbrowser.open("https://google.com/search?q=%s" % query)



from datetime import datetime
print(datetime.now())
#print(datetime.now().strftime("Today is %A, %B %d, %Y"))
#age = int(input("What's your age? "))
age=42
year_birth = datetime.now().year - age
print("We think you were born back in %s" % year_birth)

#generate passwords

import random
characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ_!@#$%^&*()?"
chosen = random.sample(characters, 6)
password = "".join(chosen)
print(password)


while True:
    #psw = input("Enter new password: ")
    psw = "shR11"
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")
        break
    else:
        print("Password is not fine")

while True:
    notes = []
   # psw = input("Enter password: ")
    psw= "shR11"
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)

import glob
file_list=glob.glob1("/Users/shravannidankavi/python lab/", "*.py")
print(len(file_list))


import glob
 
file_list = glob.glob("/Users/shravannidankavi/python lab/subdirs/**/*.py", recursive=True)
print(len(file_list))