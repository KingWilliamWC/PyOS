try:
    from System import *
    import shutil
except ImportError as e:
    print("An Error occured, " + str(e))

def evalInput(userInput):
    if userInput[0] == "cd":
        moveCWDTo(getCWD() + "/" + userInput[1])
    elif userInput[0] == "ls":
        files = listCWD()
        for f in files:
            print(f)
    elif userInput[0] == "touch":
        makeFile(userInput[1])
    elif userInput[0] == "mkdir":
        makeFolder(userInput[1])
    else:
        print("'{}' was not recognised as a valid command,\n type help for help\n".format(' '.join(userInput)))



def shell():
    end = False
    while end != True:
        userInput = input(getCWD() + ">")

        evalInput(userInput.split(" "))