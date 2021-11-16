
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Import Modules
from time import sleep
import sys
from random import choice, randint
import getpass
fileout = 0
#Functions
def fileinput_encrypt():
    try:
        fileout = 1
        filename = input("Enter the filename to encrypt: ")
        key = int(input("Enter a key: "))
        file = open(filename, "r")
        text = file.read()
        encrypt(text,key,fileout)
    except FileNotFoundError:
        print("The File You Entered Couldn't Be Found")
    except ValueError:
        print("Crypta: A Key MUST Be Integers ONLY")
      
def fileinput_decrypt():
  fileout = 1
  filename = input("Enter the filename to encrypt: ")
  key = int(input("Enter a key: "))
  file = open(filename, "r")
  text = file.read()
  decrypt(text,key,fileout)
def diffie_hellman():
    base = 34775689 #Public base number
    modulo = 10000019
    exponent = 0

    print("1, Generate Private Keyhalf \n 2, Generate Full Keyhalf \n 3, Quit")
    mode = int(input("Select Mode: "))
    if mode == 1:
        exponent = int(getpass.getpass("Enter your private exponent: "))
        result = (base**exponent)%modulo
        print("Your Halfkey is:",str(result), "and the exponent used was:",str(exponent), "remember this for the full key generation.")
    if mode == 2:
        rephkey = int(input("Enter the recived halfkey:"))
        expoused = int(getpass.getpass("Enter the exponent used when you sent you half key to them: "))
        fullkey = ((base ** expoused)%modulo)^rephkey
        print("The full key for this recipient is:",str(fullkey))
    else:
        pass
def encrypt(text,key,fileout):
    #DO NOT EDIT THE BELOW STRINGS AS THIS INCLUDES THE RELEVANT LETTERS NUMBERS AND SYMBOLS FOR THE PROGRAM.
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    capbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbet = '0123456789'
    symbet = '.,:/\!"£$%^&*()-+[]{}@#~?<>|¬`@'
    otherbet = 'łe¶ŧ←↓→øþæßðđŋħĸł«»¢“”nµ'
    newMessage = ''
    roundno = int((int(key)**5)-int(key))
    try:
        #Main code here
        message = text[::-1].swapcase() 
        key = int(key)
        #key - 15987
        key1 = key #Copies the key
        #Below takes the message and shifts it with the key
        for character in message:
            print(key , roundno)
            #Lowercase Letters
            if character in alphabet:
                position = alphabet.find(character)
                newPosition = (position + key) % 26
                newCharacter = alphabet[newPosition]
                key = key + roundno #Advances the key by the roundno (Every time a letter is processed)
                newMessage += newCharacter
            #Uppercase Letters
            elif character in capbet:
                position = capbet.find(character)
                newPosition = (position - key) % 26
                newCharacter = capbet[newPosition]
                key = key + roundno
                newMessage += newCharacter
            #Other Symbols
            elif character in otherbet:
                position = otherbet.find(character)
                newPosition = (position + key) % 26
                newCharacter = otherbet[newPosition]
                key = key + roundno
                newMessage += newCharacter
            #Numbers
            elif character in numbet:
                position = numbet.find(character)
                newPosition = (position + key) % 10
                newCharacter = numbet[newPosition]
                key = key - roundno
                newMessage += newCharacter
            #Symbols w/ number keys eg: !
            elif character in symbet:
                position = symbet.find(character)
                newPosition = (position + key) % 10
                newCharacter = symbet[newPosition]
                key = key - roundno
                newMessage += newCharacter
            #If he letter isn't in the above regions it is added as plain text
            else:
                newMessage += character 
            roundno = roundno + 1
            #newMessage = newMessage.swapcase()
        if fileout == 0:
          print("*"*20)
          print('Output: ', newMessage)
          sleep(0.002)
          print("*"*20)
        else:
          filename = input("Enter the name of the encrypted file: ")
          savefile = open(filename,"w")
          savefile.write(newMessage)
          savefile.close()
    except ValueError:
        print("Crypta: Incorrect Values Inputted Please try again")
    

    #Start of the decrypt function
def decrypt(text,key,fileout):
    message = text#.swapcase()
    

    sleep(0.25)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    capbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbet = '0123456789'
    symbet = '.,:/\!"£$%^&*()-+[]{}@#~?<>|'
    otherbet = '@łe¶ŧ←↓→øþæßðđŋħĸł«»¢“”nµ'
    newMessage = ''
    roundno = int((int(key)**5)-int(key))
    key = key
    key = "-" + str(key)
    key = int(key)
    print(key)

    key = int(key)

    for character in message:
        print(key , roundno)
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + key) % 26
            newCharacter = alphabet[newPosition]
            key = key - roundno
            newMessage += newCharacter
        elif character in capbet:
            position = capbet.find(character)
            newPosition = (position - key) % 26
            newCharacter = capbet[newPosition]
            key = key - roundno
            newMessage += newCharacter
        elif character in otherbet:
            position = otherbet.find(character)
            newPosition = (position + key) % 26
            newCharacter = otherbet[newPosition]
            key = key - roundno
        elif character in numbet:
            position = numbet.find(character)
            newPosition = (position + key) % 10
            newCharacter = numbet[newPosition]
            key = key + roundno
            newMessage += newCharacter
        elif character in symbet:
            position = symbet.find(character)
            newPosition = (position + key) % 10
            newCharacter = symbet[newPosition]
            key = key + roundno
            newMessage += newCharacter
        else:
            newMessage += character
        roundno = roundno + 1
    if fileout == 0:
      print("*"*20)
      print('Output: ', newMessage[::-1].swapcase())
      sleep(0.002)
      print("*"*20)
    else:
      filename = input("Enter the name of the encrypted file: ")
      savefile = open(filename,"w")
      savefile.write(newMessage[::-1].swapcase())
      savefile.close()
#Main Code
try:
    mode = sys.argv[1]
    if mode == "--help":
        helpmenu = open("help_menu.txt","r")
        print(helpmenu.read())
    elif mode == "-e" or mode == "-d":
        text = input("message>")
        if mode == "-e":
          key = int(getpass.getpass("key>"))
          encrypt(text,key)
        elif mode == "-d":
          key = int(getpass.getpass("key>"))
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
        print("-e = encrypt\n-d = decrypt\n-ef = Encrypt File\n-df = Decrypt File\n--help = help menu\n-dh = open diffie hellman keygen\ntype \"quit\" to exit")
        print("-"*20)
        text_mode = input("crypta>")
        if text_mode == "--help":
            helpmenu = open("help_menu.txt","r")
            print(helpmenu.read())

        elif text_mode == "-e":
            #Calls the Encrypt function
            try:
                text = input("message>")
                key = int(input("key>"))
                encrypt(text,key,fileout)
            except ValueError:
                print("Crypta: A Key MUST Be Integers ONLY")
                
        elif text_mode == "-d":
            #Calls the Decrypt function
            try:
                text = input("message>")
                key = int(input("key>"))
                decrypt(text,key,fileout)
            except ValueError:
                print("Crypta: A Key MUST Be Integers ONLY")
                
        elif text_mode == "-dh":
            print("Diffie-Hellman Keygen (BETA)")
            diffie_hellman()
            
        elif text_mode == "-ef":
            fileinput_encrypt()
            
        elif text_mode == "-df":
            fileinput_decrypt()
            
        elif text_mode == "quit":
            break
            exit()
        else:
            print("Crypta: Incorrect parameters used please see the help menu") 
      


