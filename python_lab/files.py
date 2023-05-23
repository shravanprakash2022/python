f = open("/Users/shravannidankavi/Downloads/word.txt", "r")
print(f.read())

print(f.readlines())

f.read()
 
f.seek(0)
 
print(f.read())

f.read(5)
 
print(f.tell())

print(f.mode)   
 
print(f.mode)

f = open("/Users/shravannidankavi/Downloads/word.txt", "w")
f.write("python")

#print(f.read()) 
f.write("python")
f.close() 

f = open("/Users/shravannidankavi/Downloads/word.txt", "w")
f.writelines(['python', ' ', 'and', ' ', 'java'])
f.close()

 

with open("/Users/shravannidankavi/Downloads/word.txt", "w") as f:
    f.writelines(['python', ' ', 'AWS', ' ', 'java'])

#f.close()
f = open("/Users/shravannidankavi/Downloads/word.txt", "w")
f.truncate()

f = open("/Users/shravannidankavi/Downloads/word.txt", "r")
print(f.read())