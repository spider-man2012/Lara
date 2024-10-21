#A Python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
    result=""

    #traverse text
    for i in range (len(text)):
        char=text[i]

        #encrypt Uppercase Characters
        if (char.isupper()):
            result+=chr((ord(char) + s-65) % 26 + 65)

        #Encrypt lowercase characters
        else:
            result += chr((ord(char) + s-97) % 26 + 97)

    return result

#Check the above function
text=input("Enter the text to Encrypt: ")
s=2
print("Text : "+text)
str(s)
print("Cipher Text: "+encrypt(text,s))
