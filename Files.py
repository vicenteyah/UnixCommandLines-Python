import lorem
import os
import subprocess
from time import sleep

def menu():
    menu ="""
    -- MENU --> please type an option
    [ 1 ] - Create /copy files and directories
    [ 2 ] - Shows the oldest and most current file.
    [ 3 ] - Show smaller and larger file
    [ 4 ] - Concatenate 2 files( cp , cat)
    [ 5 ] - leave

    """
    print(menu);

def selectMenu():
    while True:
        menu()
        option = int(input("type an option: "))
        if option == 1:
            createFiles_and_dirs()
        elif option == 2:
            oldest = input("please type the name od directory to know what is the oldest file: ")
            current = input("please type the name of directory to consult the recent file: ")
            get_oldestFile(oldest)
            get_currentFile(current)
        elif option == 3:
            getSizes()
            pass
        elif option == 4:
            pass
        elif option == 5:
            sleep(1)
            print("goodbye...........")
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
    
    
def get_oldestFile(DirNam):
    print("The oldest file in: "+DirNam)
    os.system("cd {0} && ls -ltr | head -n 2".format(DirNam))


def get_currentFile(DirNam):
    print('The crrent file in: '+DirNam)
    os.system("cd {0} && ls -lt | head -n 2".format(DirNam))

def getSizes():
    s_dir = input("Ingrese nombre del directorio para consultar el archivo más pequeño: ")
    b_dir = input("Ingrese nombre del directorio para consultar el archivo más grande: ")

    s_file = os.popen('cd {0}/{1} &&  du -bhs * | sort -n | head -1'.format("UnixFile-Management-python",b_dir)).read()
    print(s_file.split('\n')[0] + " --> Es el archivo más pequeño del directorio " + s_dir)
    b_file = os.popen('cd {0}/{1} && du -bhs * | sort -nr | head -1'.format("UnixFile-Management-python",b_dir)).read()
    print(b_file.split('\n')[0] + " --> Es el archivo más grande del directorio " + b_dir)


