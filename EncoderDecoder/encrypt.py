import os
currentDir = os.path.realpath(os.path.dirname(__file__))
delimiter = '|' # could use = u"\u2063" for non visible delimiter
def encrypt(filepath,passcode=0):
    passcode = int(passcode)
    encryptedtext = []
    try:
        os.mkdir(currentDir+r"\output")
    except OSError as e:
        print("Couldnt create new output directory: ",e)
    #### Encryption part ####
    try:
        file = open(file=filepath,mode="r")
        read = file.read()
        if passcode > 0:
            for i in read:
                encryptedtext.append((str((ord(i)+567)+passcode)))
        else:
            for i in read:
                encryptedtext.append((str(ord(i)+567)))
        file.close()
    except Exception as e:
        print("Couldnt encrypt file: ",e)
        file.close()
    #### End of encryption part ####
    try:
        outputfile = open(currentDir+"\output\output.jul",mode="x")
        outputfile.write(delimiter.join(encryptedtext))
    except Exception as e:
        print("Could not output encrypted file: ",e)


def decrypt(filepath,passcode=0):
    passcode = int(passcode)
    decryptedtext = []
    try:
        os.mkdir(currentDir+r"\output")
    except OSError as e:
        print("Couldnt create output directory: ",e)
    #### Decryption part ####
    try:
        encryptedfile = open(file=filepath,mode="r")
        read = encryptedfile.read().split(sep=delimiter)
        if passcode > 0:
            for i in read:
                decryptedtext.append(chr((int(i)-passcode)-567))
        else:
            for i in read:
                decryptedtext.append(chr(int(i)-567))
        encryptedfile.close()
    except Exception as e:
        print("Could not decrypt file: ",e)
        encryptedfile.close()
    #### End of decryption part ####
    try:
        outputfile = open(currentDir+"\output\output.txt",mode="x")
        outputfile.write("".join(decryptedtext))
    except Exception as e:
        print(e)

print("Encrypt: encrypt filepath optional:passcode")
print("Decrypt: decrypt filepath optional:passcode")
inp = input().replace('"', '')
args = []
if "encrypt" in inp.lower():
    for i in range(1,len(inp.split())):
       args.append(inp.split()[i])
    try:
        if len(args) == 1:
            encrypt(args[0])
        elif len(args) == 2:
            encrypt(args[0], args[1])
        else:
            print("Too many or little arguments")
    except Exception as e:
        print("Couldnt execute encrypt command",e)
elif "decrypt" in inp.lower():
    for i in range(1,len(inp.split())):
        args.append(inp.split()[i])
    try:
        if len(args) == 1:
            decrypt(args[0])
        elif len(args) == 2:
            decrypt(args[0], args[1])
        else:
            print("Not enough arguments")
    except Exception as e:
        print("Couldnt execute decrypt command",e)
else:
    print("Unrecognized command")

input("Press enter to exit")