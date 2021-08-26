#Key splitter for Crypta 2.01


#Key Splitter Function
def key_splitter(key):
    loop = 0 #Set the loop counter to 0
    key1 = "" #Set the key values to be empty
    key2 = ""
    for character in key: #Iterates through the key
        if (loop % 2) == 0: #If the loop number is even
            key1 = key1 + character #Add the number to key1
            loop = loop + 1
        elif (loop % 2) == 1: #If the loop no is odd
            key2 = key2 + character #Add the character to key2
            loop = loop + 1
        else:
            break #If it errors break the cycle
    return int(key1), int(key2) #Return the keys as ints

#Test implementation of the code
while True:
    key = input("Enter the key: ")
    result = key_splitter(key) #This is how you should call the function
    print(result)

