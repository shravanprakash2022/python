#Encryption password 
def enc_pass():
    #password = input("what is your password? ")
    password = input("enter a letter ")
    key = int(input("what is your encryption key to decode? "))
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    if password.index == letters.index:
        encoded_pass = letters[key]
        print(encoded_pass)


'''
    print(password)
    if password in letters:
        #password = letters.index(key)
        password = password + letters[key]
        print(password)
        return password
'''

''' for i in password:
        i[index] == i[index] + letters[key]
        index += 1
        i += 1
        return i
'''


enc_pass()