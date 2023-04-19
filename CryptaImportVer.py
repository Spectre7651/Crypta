 #Notes


#Imports




#Functions/precedures

#-------------------------------------------------------------
#Encrypt Mode
def enc(key,message):
    key = int(key)
    messagelen = len(message)
    oldroundkey = 1
    newMessage = ""
    i = 0
    for character in message:
        i = i + 1
        roundkey = int(randnums[((i+23)%len(randnums))])+ (key + int(randnums[(oldroundkey % len(randnums))])) # key for the round is generated
        oldroundkey = roundkey
        #print("RND: ",roundkey)
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + roundkey) % len(alphabet)
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
        #Uppercase Letters
        elif character in capbet:
            position = capbet.find(character)
            newPosition = (position + roundkey) % len(capbet)
            newCharacter = capbet[newPosition]
            newMessage += newCharacter
        #Numbers
        elif character in numbet:
            position = numbet.find(character)
            newPosition = (position + roundkey) % len(numbet)
            newCharacter = numbet[newPosition]
            newMessage += newCharacter
        #Symbols w/ number keys eg: !
        elif character in symbet:
            position = symbet.find(character)
            newPosition = (position + roundkey) % len(symbet)
            newCharacter = symbet[newPosition]
            newMessage += newCharacter
        #If he letter isn't in the above regions it is added as plain text
        else:
            newMessage += character
    return newMessage

#------------------------------------------------------------
#Decrypt Mode
def dec(key,message):
    key = int(key)
    messagelen = len(message)
    oldroundkey = 1
    newMessage = ""
    i = 0
    for character in message:
        i = i + 1
        roundkey = int(randnums[((i+23)%len(randnums))])+ (key + int(randnums[(oldroundkey % len(randnums))])) # key for the round is generated
        oldroundkey = roundkey
        roundkey = "-" + str(roundkey)
        roundkey = int(roundkey)
        #print("RND: ",roundkey)
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + roundkey) % len(alphabet)
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
        #Uppercase Letters
        elif character in capbet:
            position = capbet.find(character)
            newPosition = (position + roundkey) % len(capbet)
            newCharacter = capbet[newPosition]
            newMessage += newCharacter
        #Numbers
        elif character in numbet:
            position = numbet.find(character)
            newPosition = (position + roundkey) % len(numbet)
            newCharacter = numbet[newPosition]
            newMessage += newCharacter
        #Symbols w/ number keys eg: !
        elif character in symbet:
            position = symbet.find(character)
            newPosition = (position + roundkey) % len(symbet)
            newCharacter = symbet[newPosition]
            newMessage += newCharacter
        #If he letter isn't in the above regions it is added as plain text
        else:
            newMessage += character
    return newMessage
#-------------------------------------------------------------
#Output the results of string encrypt/decryption
def outputdata(data,function):
    print("-"*20)
    if function == "enc":
        print("Encrypted Message: {}".format(data))
    else:
        print("Plaintext Message: {}".format(data))
#Global data
global alphabet
global capbet
global numbet
global symbet
global randnums
alphabet = 'abcdefghijklmnopqrstuvwxyz'
capbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbet = '0123456789'
symbet = '.,:/\!"£$%^&*()-+[]@#~?<>|¬`@łe¶ŧ←↓→øþæßðđŋħĸł«»¢“”nµ'
randnumfile = open("randomnums.txt","r")
randnums = randnumfile.read()

