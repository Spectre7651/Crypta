 #Notes


#Imports




#Functions/precedures

#-------------------------------------------------------------
#Encrypt Mode
def enc(key,message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    capbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbet = '0123456789'
    symbet = '.,:/\!"£$%^&*()-+[]@#~?<>|¬`@łe¶ŧ←↓→øþæßðđŋħĸł«»¢“”nµ'
    groupkeyfile = open("groupkey.txt","r")
    groupkey = groupkeyfile.read()
    key = int(key)
    messagelen = len(message)
    oldroundkey = 1
    newMessage = ""
    i = 0
    for character in message:
        i = i + 1
        roundkey = int(groupkey[((i+23)%len(groupkey))])+ (key + int(groupkey[(oldroundkey % len(groupkey))])) # key for the round is generated
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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    capbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbet = '0123456789'
    symbet = '.,:/\!"£$%^&*()-+[]@#~?<>|¬`@łe¶ŧ←↓→øþæßðđŋħĸł«»¢“”nµ'
    groupkeyfile = open("groupkey.txt","r")
    groupkey = groupkeyfile.read()
    key = int(key)
    messagelen = len(message)
    oldroundkey = 1
    newMessage = ""
    i = 0
    for character in message:
        i = i + 1
        roundkey = int(groupkey[((i+23)%len(groupkey))])+ (key + int(groupkey[(oldroundkey % len(groupkey))])) # key for the round is generated
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
global alphabet
global capbet
global numbet
global symbet
global groupkey
alphabet = 'abcdefghijklmnopqrstuvwxyz'
capbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbet = '0123456789'
symbet = '.,:/\!"£$%^&*()-+[]@#~?<>|¬`@łe¶ŧ←↓→øþæßðđŋħĸł«»¢“”nµ'
groupkeyfile = open("groupkey.txt","r")
groupkey = groupkeyfile.read()

