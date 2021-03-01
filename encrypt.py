#Import modules
from random import choice
from time import sleep

#DO NOT EDIT THE BELOW STRINGS AS THIS INCLUDES THE RELEVANT LETTERS NUMBERS AND SYMBOLS FOR THE PROGRAM.
keychoice = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
capbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbet = '0123456789'
symbet = '.,:/\!"£$%^&*()-+[]{}@#~?<>|¬`'
otherbet = '@łe¶ŧ←↓→øþæßðđŋħĸł«»¢“”nµ'
newMessage = ''
#Main code here
print("Crypta \nEncoding Software Loading... \n Version: 1.0")
print("--------------------------------")
sleep(0.5)
message = input('Please enter a message: ') 
key = int(choice(keychoice))#Generates the random key
key1 = key #Copies the key
#Below takes the message and shifts it with a randomly generated key
for character in message:
    #Lowercase Letters
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        key = key + 1 #Advances the key by 1 (Every time a letter is processed)
        newMessage += newCharacter
    #Uppercase Letters
    elif character in capbet:
        position = capbet.find(character)
        newPosition = (position + key) % 26
        newCharacter = capbet[newPosition]
        key = key + 1
        newMessage += newCharacter
    #Other Symbols
    elif character in otherbet:
        position = otherbet.find(character)
        newPosition = (position + key) % 26
        newCharacter = otherbet[newPosition]
        key = key + 1
        newMessage += newCharacter
    #Numbers
    elif character in numbet:
        position = numbet.find(character)
        newPosition = (position + key) % 9
        newCharacter = numbet[newPosition]
        key = key + 1
        newMessage += newCharacter
    #Symbols w/ number keys eg: !
    elif character in symbet:
        position = symbet.find(character)
        newPosition = (position + key) % 9
        newCharacter = symbet[newPosition]
        key = key + 1
        newMessage += newCharacter
    #If he letter isn't in the above regions it is added as plain text
    else:
        newMessage += character
key1 = key1 + 785643 #obscures the message but will be improved with encoding / encryption 
key1 = str(key1)
key1 = "-"+ key1 #Makes the key negative for decoding



print('Output: ', newMessage)
sleep(0.002)
print('You private key is:' , key1 , "\n Give this code to the recipient so they can decode it")

   
