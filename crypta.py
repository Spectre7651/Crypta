#Command script for Crypta
#   Possible commands:
#       -e Encrypt
#       -d Decrypt
#       --help Open help menu
#
#   Example command (Run from cmd line)
#       python3 crypta.py -e hello there this is a secret code
#
#   If no arguments are supplied then it brings up an interactive cli view
#   See --help for more info
#Import Modules
from time import sleep
import sys
from random import choice
import base64

#Functions
def encrypt(text):
    #DO NOT EDIT THE BELOW STRINGS AS THIS INCLUDES THE RELEVANT LETTERS NUMBERS AND SYMBOLS FOR THE PROGRAM.
    keychoice = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    capbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbet = '0123456789'
    symbet = '.,:/\!"£$%^&*()-+[]{}@#~?<>|¬`'
    otherbet = '@łe¶ŧ←↓→øþæßðđŋħĸł«»¢“”nµ'
    newMessage = ''
    #Main code here
    message = text 
    key = int(choice(keychoice))#Generates the random key
    key1 = key #Copies the key
    #Below takes the message and shifts it with the randomly generated key
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
            newPosition = (position + key) % 10
            newCharacter = numbet[newPosition]
            key = key + 1
            newMessage += newCharacter
        #Symbols w/ number keys eg: !
        elif character in symbet:
            position = symbet.find(character)
            newPosition = (position + key) % 10
            newCharacter = symbet[newPosition]
            key = key + 1
            newMessage += newCharacter
        #If he letter isn't in the above regions it is added as plain text
        else:
            newMessage += character 
    
    key1 = str(key1)
    key1 = "-"+ key1 #Makes the key negative for decoding
    key1 = int(key1) - 15987 #obscures the key
    #key1 = key1.encode()
    #key1 = base64.b64encode(key1)


    print('Output: ', newMessage)
    sleep(0.002)
    print('You private key is:' , key1 , "\n Give this code to the recipient so they can decode it\n")
    #save_key = input("Do you want to save the encrpytion key encoded format? [Y/n]")
    #save_key = save_key.lower()
    #if save_key == "y":
      #filename = "crypta_encoded_key_"+dt
      #file = open(filename , "a")
      #file.write(dt+"\n==Key Start== \n"+key1+"\n==Key End==")
    
#Start of the decrypt function
def decrypt(text,key):
    message = text

    sleep(0.25)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    capbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbet = '0123456789'
    symbet = '.,:/\!"£$%^&*()-+[]{}@#~?<>|'
    otherbet = '@łe¶ŧ←↓→øþæßðđŋħĸł«»¢“”nµ'
    newMessage = ''
    key = key
    #key = base64.b64decode(key)
    #key = key.decode()
    key = int(key)
    key = key + 15987

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
            newPosition = (position + key) % 10
            newCharacter = numbet[newPosition]
            key = key - 1
            newMessage += newCharacter
        elif character in symbet:
            position = symbet.find(character)
            newPosition = (position + key) % 10
            newCharacter = symbet[newPosition]
            key = key - 1
            newMessage += newCharacter
        else:
            newMessage += character

    print('Original Message : ', newMessage)
#Main Code
try:
    mode = sys.argv[1]
    if mode == "--help":
        helpmenu = open("help_menu.txt","r")
        print(helpmenu.read())
    elif mode == "-e" or mode == "-d":
        text = input("message>")
        if mode == "-e":
          encrypt(text)
        elif mode == "-d":
          key = int(input("key>"))
          decrypt(text,key)
        elif IndexError:
          print("Crypta: Missing/Wrong Parameters see --help")
    else:
        print("Crypta: Incorrect parameters used please see --help")
except IndexError:
    print("No parameters found defaulted to cli view")
    print("-" * 20)
    print("Crypta Command Line Interface Version 1.7")
    cli = "run"
    while cli == "run":
        print("-"*20)
        print("-e = encrypt\n-d = decrypt\n--help = help menu\ntype \"quit\" to exit")
        print("-"*20)
        text_mode = input("crypta>")
        if text_mode == "--help":
            helpmenu = open("help_menu.txt","r")
            print(helpmenu.read())
        elif text_mode == "-e":
            text = input("message>")
            encrypt(text)
        elif text_mode == "-d":
            text = input("message>")
            key = int(input("key>"))
            decrypt(text,key)
        elif text_mode == "quit":
            break
            exit()
        else:
            print("Crypta: Incorrect parameters used please see the help menu")
            
