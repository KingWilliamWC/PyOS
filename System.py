import sys
import os
import shutil
def getCWD():
    cwd = os.getcwd()
    return cwd

def moveCWDTo(destination):
    os.chdir(destination)

def listCWD():
    return os.listdir()

def makeFile(fileName):
    open(fileName, 'a').close()

def makeFolder(folderName):
    os.mkdir(folderName)