import lorem
import os
import subprocess
from time import sleep

def menu():
    menu ="""
    -- MENU --> please type an option
    [ 1 ] - Create /copy files and directories
    [ 2 ] - Show the oldest file and most lasted
    [ 3 ] - leave

    """
    print(menu);

def createDirectory(directoryName):
    subprocess.call(["mkdir", directoryName])


def createfile(fileName):
    subprocess.call(["touch", fileName])
    os.system('echo' + lorem.paragraph() + ' > ' + fileName)

