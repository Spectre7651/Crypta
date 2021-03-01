#I havent annotated this script as its very similar to encode.py apart from the commented things.
from time import sleep
from random import sleep
print("Crypta \nDecoding Software Loading... \n Version: 1.0")
print("--------------------------------")
sleep(0.5)
message = input('Please enter a message: ')

sleep(0.25)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
capbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbet = '0123456789'
symbet = '.,:/\!"£$%^&*()-+[]{}@#~?<>|'
otherbet = '@łe¶ŧ←↓→øþæßðđŋħĸł«»¢“”nµ'
newMessage = ''
key = input("Enter the secret key: ")
key = int(key)
key = key + 785643 #This un-obscures the key (Again will make it better)

key = int(key)

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        key = key - 1 #Subtracts 1 from the key
        newMessage += newCharacter
    elif character in capbet:
        position = capbet.find(character)
        newPosition = (position + key) % 26
        newCharacter = capbet[newPosition]
        key = key - 1
        newMessage += newCharacter
    elif character in otherbet:
        position = otherbet.find(character)
        newPosition = (position + key) % 26
        newCharacter = otherbet[newPosition]
        key = key - 1
    elif character in numbet:
        position = numbet.find(character)
        newPosition = (position + key) % 9
        newCharacter = numbet[newPosition]
        key = key - 1
        newMessage += newCharacter
    elif character in symbet:
        position = symbet.find(character)
        newPosition = (position + key) % 9
        newCharacter = symbet[newPosition]
        key = key - 1
        newMessage += newCharacter
    else:
        newMessage += character

print('Original Message : ', newMessage)

     
