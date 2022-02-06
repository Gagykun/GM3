# Written by gagy#0404 ^_^
# Windows ONLY release
import os
import sys
import time
import zipfile
import shutil
from asyncore import write
from logging import root
from sys import path

import colorama
import requests
from colorama import Back, Fore, Style

colorama.init()

print(Fore.MAGENTA + Style.BRIGHT +"Written by Gagy (gagy#0404) with" + Fore.CYAN + " <3")
print(Style.RESET_ALL)
appDataFolder = os.getenv('APPDATA')


try:
    rootDir = (f"{appDataFolder}\.minecraft\\")
    os.chdir(rootDir)
except Exception:
    print(Fore.RED + "Unable to locate your minecraft installation folder. GM3 does not support minecraft installations installed on other than the default directory.")
    print("Exiting in 8 seconds.")
    time.sleep(8)
    sys.exit()

if os.path.exists("GMCMI"):
    os.chdir(f"{rootDir}GMCMI")
    if os.path.exists("ign.txt"):
        pass
    else:
        print(Fore.YELLOW +f"By running this tool, your entire mods folder will be deleted to ensure compatibilty with the server. To supress this warning on startup, create a file named [ign.txt] in the {rootDir}\\GMCMI\\")
        print(Style.RESET_ALL)
        print("Continuing in 10 seconds...")
        time.sleep(10)
    try:
        os.chdir(f"{rootDir}GMCMI\\inf")
    except FileNotFoundError:
        print(Fore.RED + "Potentially corrupt installation detected[3]. Re-install the program to try and fix the issue.")
        print(Style.RESET_ALL)
        sys.exit()
    except Exception as e:
        print(e)
        sys.exit()
    if os.path.exists("ver.txt"):
        f = open("ver.txt", "r")
        curVer = f.read()
        f.close()
        os.chdir(rootDir)
    else:
        try:
            print(Fore.RED + "Potentially corrupt installation detected[2]. Attempting repairs...")
            print(Style.RESET_ALL)
            url = f'http://gagy.us.to:34197/ver.txt'
            r = requests.get(url, allow_redirects=True)
            open("ver.txt", 'wb').write(r.content)
        except requests.ConnectionError:
            print(Fore.RED + "Unable to connect to the server or the request was actively rejected. Is the server down for maintenance?")
            print(Style.RESET_ALL)
            time.sleep(10)
            sys.exit()
        except Exception as e:
            print(Style.RESET_ALL)
            excFile = open("exception.txt", "w")
            excFile.write(str(e))
            excFile.close()
            print(Fore.RED + f"An exception occured while trying to fix error[2]. Please send the [error2.txt] located in to gagy#0404 on Discord.")
            print(Fore.YELLOW + Style.BRIGHT + "Your username and some personal information may be included in the error report.")
            print(Style.RESET_ALL)
            time.sleep(10)
            sys.exit()
        print(Fore.GREEN + "An attempt to fix the error was made. Please restart GM3.")
        time.sleep(5)
        sys.exit()

else:
    print(Fore.YELLOW +f"By running this tool, your entire mods folder will be deleted to ensure compatibilty with the server.")
    print(Style.RESET_ALL)
    print("Continuing in 10 seconds...")
    time.sleep(10)
    os.chdir(rootDir)
    print(Fore.YELLOW +"First time run detected, setting up FS")
    print(Style.RESET_ALL)
    os.mkdir("GMCMI")
    os.chdir("GMCMI")
    os.mkdir("inf")
    os.chdir(rootDir)
    print(Fore.GREEN +"FS done!")
    print(Style.RESET_ALL)

print(Fore.YELLOW + "Checking for updates...")
print(Style.RESET_ALL)

try: # try loop for active server connection, if fail, exit program
    os.chdir(f"{rootDir}GMCMI//inf")
    url = f'http://gagy.us.to:34197/ver.txt'
    r = requests.get(url, allow_redirects=True)
    open("ver.txt", 'wb').write(r.content)
    f = open("ver.txt", "r")
    ver = f.read()
    f.close()
except requests.ConnectionError:
    print(Fore.RED + "Unable to connect to the server or the request was actively rejected. Is the server down for maintenance?")
    print(Style.RESET_ALL)
    time.sleep(10)
    sys.exit()
# We do not delete the ver.txt just yet
try:
    if ver == curVer: # Compares what version we have installed
        print(Fore.GREEN+"You are on the latest version.")
        print(Style.RESET_ALL)
        print(Fore.MAGENTA + f"Server: {ver}" + Fore.GREEN + " - " + f"Client: {curVer}")
        print(Style.RESET_ALL)
        print("Closing in 5 seconds")
        time.sleep(5)
        sys.exit()
except NameError:
    #print(Fore.YELLOW + "Unable to locate a previous update version. Most likely a first time installation Installing anyway.")
    print(Style.RESET_ALL)

print(Fore.GREEN+"Found an update.")
print(Style.RESET_ALL)
print(Fore.YELLOW + "Downloading mods...")
print(Style.RESET_ALL)
os.chdir(f"{rootDir}GMCMI")
url = f'http://gagy.us.to:34197/mods.zip'
r = requests.get(url, allow_redirects=True)
open("mods.zip", 'wb').write(r.content)
print(Fore.YELLOW + "Extracting files... This may take a while depending on your systems specifications...")
print(Style.RESET_ALL)
try:
    os.chdir(f"{rootDir}mods")
except Exception:
    print(Fore.YELLOW + "You are missing the [mods] folder. We have created a mods folder for you but you must install minecraft forge yourself." + "\n" + "Resuming in 3 seconds.")
    print(Style.RESET_ALL)
    time.sleep(5)
try:
    shutil.rmtree(f"{rootDir}mods")
except FileNotFoundError:
    pass
with zipfile.ZipFile(f"{rootDir}GMCMI/mods.zip", 'r') as zip_ref:
    zip_ref.extractall(f'{rootDir}mods')
os.remove(f"{rootDir}GMCMI/mods.zip")
#print(chr(27) + "[2J")
print(Fore.GREEN+"Finished updating mods. You are now up to date!")
print(Style.RESET_ALL)
print("Closing in 5 seconds")
time.sleep(5)
sys.exit()
