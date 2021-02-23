# Written by gagy#0404 ^_^
# Windows ONLY release
from sys import path
import colorama
import requests
import sys
import time
import os
from colorama import Fore, Back, Style
import zipfile
from shutil import copyfile
colorama.init()

print(Fore.MAGENTA + Style.BRIGHT +"Written by Gagy (gagy#0404)")
print(Style.RESET_ALL)
rootDir = os.getcwd()

os.chdir("..")
if os.path.exists("GMCMI"):
    os.chdir(rootDir)
    if os.path.exists("ign.txt"):
        pass
    else:
        print(Fore.YELLOW +"By running this tool, your entire mods folder will be deleted to ensure compatibilty with the server. To supress this warning on startup, create a file named [ign.txt] in the same directory where GMCMI.exe is located.")
        print(Style.RESET_ALL)
        print("Continuing in 10 seconds...")
        time.sleep(10)
    try:
        os.chdir("inf")
    except FileNotFoundError:
        print(Fore.RED + "Potentially corrupt instalation detected[3]. Re-install the program to try and fix the issue.")
        print(Style.RESET_ALL)
        sys.exit()
    if os.path.exists("ver.txt"):
        f = open("ver.txt", "r")
        curVer = f.read()
        f.close()
        os.chdir(f"{rootDir}")
    else:
        print(Fore.RED + "Potentially corrupt instalation detected[2]. Re-install the program to try and fix the issue.")
        print(Style.RESET_ALL)
        time.sleep(7)
        sys.exit()

else:
    os.chdir(rootDir)
    print(Fore.YELLOW +"First time run detected, setting up FS")
    print(Style.RESET_ALL)
    os.mkdir("GMCMI")
    os.chdir("GMCMI")
    os.mkdir("inf")
    os.chdir(rootDir)
    print(Fore.GREEN +"FS done!")
    print(Style.RESET_ALL)

print(Fore.YELLOW + "Checking for updates.")
print(Style.RESET_ALL)

try: # try loop for active server connection, if fail, exit program
    url = f'http://play.ogcraft.us.to:34197/ver.txt'
    r = requests.get(url, allow_redirects=True)
    open("ver.txt", 'wb').write(r.content)
    f = open("ver.txt", "r")
    ver = f.read()
    f.close()
except requests.ConnectionError:
    print(Fore.RED + "The server actively refused the connection. Is the server down for maintenance?")
    print(Style.RESET_ALL)
    time.sleep(7)
    sys.exit()
# We do not delete the ver.txt just yet
try:
    if ver == curVer: # Compares what version we have installed
        print(Fore.GREEN+"You are on the latest version.")
        print(Style.RESET_ALL)
        os.remove("ver.txt")
        print("Closing in 5 seconds")
        time.sleep(5)
        sys.exit()
except NameError:
    print(Fore.YELLOW + "Previous version not found, most likely fresh install. Installing anyway.")
    print(Style.RESET_ALL)

print(Fore.GREEN+"Found an update.")
print(Style.RESET_ALL)
print(Fore.YELLOW + "Downloading mods...")
print(Style.RESET_ALL)
url = f'http://play.ogcraft.us.to:34197/mods.zip'
r = requests.get(url, allow_redirects=True)
open("mods.zip", 'wb').write(r.content)
print(Fore.YELLOW + "Extracting. This may take a while depending on your systems specifications...")
print(Style.RESET_ALL)
apD = os.getenv('APPDATA')
os.system(f"rmdir /Q /S {apD}/.minecraft/mods")
with zipfile.ZipFile(f"{rootDir}/mods.zip", 'r') as zip_ref:
    zip_ref.extractall(f'{apD}/.minecraft/mods')
os.remove("mods.zip")
os.system(f"move ver.txt GMCMI/inf")
os.system(f"move GMCMI.exe GMCMI/")
#print(chr(27) + "[2J")
print(Fore.GREEN+"Mods are now up to date!")
print(Style.RESET_ALL)
print("Closing in 5 seconds")
time.sleep(5)
sys.exit()