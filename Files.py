import lorem
import os
import subprocess
from time import sleep

def menu():
    menu ="""
    -- MENU --> please type an option
    [ 1 ] - Create /copy files and directories
    [ 2 ] - Shows the oldest and most current file.
    [ 3 ] - Concatenate 2 files( cp , cat)
    [ 4 ] - leave

    """
    print(menu);

def selectMenu():
    while True:
        menu()
        option = int(input("type an option: "))
        if option == 1:
            createFiles_and_dirs()
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            break

#create a folder
def createDirectory(directoryName):
    subprocess.call(["mkdir", directoryName])

#This function creates a file with text auto generated
def createfile(fileName):
    subprocess.call(["touch", fileName])
    os.system('echo ' + lorem.paragraph() + ' > ' + fileName)

#This function creates files and directories using the previous functions
def createFiles_and_dirs():
    dirs = ["DirA","DirB"]
    nameA = ["A1","A2","A3"]
    nameB = ["B1", "B2", "B3"]
    for dirs in dirs:
        createDirectory(dirs)
        sleep(2)
    
    for nameA in nameA:
        sleep(2)
        createfile("DirA" + "/" + nameA + ".txt")
    
    for nameB in nameB:
        sleep(2)
        createfile("DirB" + "/" + nameB + ".txt")
    
    



