 #Notes


#Imports
from CryptaFileHandling import encryptfile, decryptfile
from CryptaCipher import enc,dec



#Functions/precedures
#Output the results of string encrypt/decryption
def outputdata(data,function):
    print("-"*20)
    if function == "enc":
        print("Encrypted Message: {}".format(data))
    else:
        print("Plaintext Message: {}".format(data))
#------------------------------------------------------------
#Main Program

while True:
    try:
        print("\nCrypta Command Line Interface V3.1")
        print("----------------------------------")
        print("-e = Encrypt Message")
        print("-d = Decypt Message")
        print("-ef = Encrypt File")
        print("Press ctrl-c to exit")
        mode = input("$ ")
        try:
            try:
                md = mode[1] + mode[2]
                md = md.lower()
            except IndexError:
                md = mode[1]
                md = md.lower()
            if md == "e":
                print("Encrypt Mode")
                message = input("message> ")
                try:
                    key = int(input("key> "))
                except ValueError:
                    print("The Key MUST be integers")
                    key = int(input("key>> "))
                message = enc(key,message)
                outputdata(message, "enc")
            elif md == "d":
                print("Decrypt Mode")
                message = input("message> ")
                try:
                    key = int(input("key> "))
                except ValueError:
                    print("The Key MUST be integers")
                    key = int(input("key>> "))
                message = dec(key,message)
                outputdata(message, "dec")
            elif md == "ef":
                print("Encrypt File")
                filename = input("filename> ")
                try:
                    key = int(input("key> "))
                except ValueError:
                    print("The Key MUST be integers")
                    key = int(input("key>> "))
                fileout = input("Enter the filename to save in> ")
                encryptfile(filename,fileout,key)
            elif md == "df":
                print("Decrypt File")
                filename = input("filename> ")
                try:
                    key = int(input("key> "))
                except ValueError:
                    print("The Key MUST be integers")
                    key = int(input("key>> "))
                fileout = input("Enter the filename to save in> ")
                decryptfile(filename,fileout,key)
            else:
                pass
        except IndexError:
            pass
        
    except KeyboardInterrupt:
        break
