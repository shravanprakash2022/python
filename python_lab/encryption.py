##1)Bigginer way

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
'''
def encrypt(text, shift):
  final_value = ""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position +  shift
    new_letter = alphabet[new_position]
    final_value += new_letter
  print (f'actual letter is "{text}", after encoding " {final_value} "')
#print(final_value)
encrypt(text, shift)

'''
#*************************
#*************************

##1)Advanced way

def ceasar(text, shift, direction):
  final_value = ""
  if direction == "decode":
    shift *=-1
  for letter in text:
    position = alphabet.index(letter)
    new_position = position +  shift
    new_letter = alphabet[new_position]
    final_value += new_letter
  print (f'Direction is "{direction}d", hence result: "{final_value}"')

x = ceasar(text, shift, direction)
print(x) 