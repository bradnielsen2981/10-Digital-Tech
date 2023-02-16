# the following globals will be read by the function but will not be changed, therefore global keyowrd will not be needed
alphabet = 'abcdefghijklmnopqrstuvwxyz'
lengthofalphabet = len(alphabet)

def findletterindex(letter):
    for index in range(lengthofalphabet):
        if alphabet[index] == letter:
            return index
    return 0

def encrypt(message, shift):
    newmessage = ""
    for letter in message:
        if letter in " !,.": # test of special characters 
            newmessage = newmessage + letter
        else:
            currentindex = findletterindex(letter) 
            newindex = (currentindex + shift)%lengthofalphabet
            newmessage = newmessage + alphabet[newindex]
    return newmessage

def decrypt(message, shift):
    newmessage = ""
    for letter in message:
        if letter in " !,.": # test of special characters 
            newmessage = newmessage + letter
        else:
            currentindex = findletterindex(letter) 
            newindex = currentindex - shift
            if newindex < 0:
                newindex = newindex + lengthofalphabet
            newmessage = newmessage + alphabet[newindex]
    return newmessage

message = encrypt("you are awesome!", 4)
print(message)
message = decrypt(message, 4)
print(message)

