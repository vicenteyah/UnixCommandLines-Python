import os
import subprocess
from time import sleep

def changePermissions():
    os.system('sudo su')
    print()
    file = input("type the file name to change the permissions in DirA: ")
    os.system('ls -lha {0}'.format("DirA"))
    os.system('sudo chmod 111 {0}/{1}'.format("DirA", file))
    sleep(1)
    os.system('ls -lha {0}\n'.format("DirA"))
    sleep(2)
    print(".......Done!")

def changeOwner(file):
    owner_name = input("Escribe el nombre del nuevo PROPIETARIO: ")
    subprocess.call(['sudo','chown', owner_name, "DirA"+'/'+file])
