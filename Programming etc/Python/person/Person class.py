from externalFuncs import formatList
import os
clear = lambda: os.system('cls')

class person:
    name = ""
    fname = ""
    lname = ""
    age = 0

    def __init__(self, name="", age=0):
            self.name = name
            self.age = age
            namearray = name.split(maxsplit=1)
            try:
                self.fname = namearray[0]
                self.lname = namearray[1]
            except:
                print("There was an error assigning the name, make sure to only include 2 words")
    def getInfo(self):
        return formatList(self.__dict__)

    def getName(self):
        return self.name
    def setName(self, nme=name):
        self.name = nme
    def createInfoFile(self):
        f = open(file="info.txt", mode="w+")
        f.write(self.getInfo)
        f.close

#To register a new command, create the command in the command list array and provide a description
#Next add the command in the command class with the exact name as provided in the command list array
#If an parameter is used it is an array of arguments provided during command execution
# for example the pr command will provide an array of words to print ex = pr Hello, World!
# Hello, World is an array of two word ["Hello,", "World!"] and each element is unpacked and printed
class commands:
    def pr(arg=""):
        print(*arg) #Asterisk * can unpack tables when placed before a table

    def help():
        for k, v in command_list.items():
            print(v)

    def cls():
        clear()

    def dp():
        print(*data_list)

    def dv():
        for k, v in var_list.items():
            print(k+"="+v)

    def var(arg=""):
        if len(arg) == 2:
            try: 
                var_list[str(arg[0])] = arg[1]
            except Exception as e:
                print("Could not add variable",e)
        else:
            print("Too many or little arguments provided, syntax follow var NAME VALUE")
        


command_list={
    "help": "help: lists commands",
    "pr": "pr: Prints out the input",
    "dp": "dp: Displays a list of current data added to the system",
    "cls" : "cls: Clears the screen of any previous text",
    "var" : "var: Add a new variable with the given value and name",
    "dv" : "dp: Displays all variables"
        }

data_list = []

var_list = {}

enabled = True
while enabled == True:
    command=input().lower()
    flags = []
    found = False
    lista = command.split()
    for i in lista:

        if command == "exit":
            enabled = False

        if i in command_list:
            found = True
            command = i
            command_class = globals()["commands"]
            func = getattr(command_class, i)
        else:
            flags.append(i)
        if found == True and i == lista[-1]:
            try:
                if len(flags) > 0:
                    func(flags)
                else:
                    func()
            except Exception as e:
                print("couldnt execute command:", e)