import os

for filename in os.listdir('.'):
    if os.path.isfile(filename):
        creation_time = os.path.getctime(filename)
        modification_time = os.path.getmtime(filename)
        print(f"{filename} (Created: {creation_time}, Modified: {modification_time})")