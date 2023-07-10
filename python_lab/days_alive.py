# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
current_age = int(age)
year = 365
max_age = 70
month = year / 12
week = year / 52
years_left = max_age - current_age
#days_left = (max_age * year) - (age * year)
days_left = years_left * 365
#weeks_left = (max_age * weeks) - (age * weeks)
weeks_left = years_left * 52
#months_left = (max_age * month) - (age * month)
months_left = years_left * 12

print(f"In {max_age} years of human life, You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
