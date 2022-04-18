<h1 align="center">
  <br>
  <a href="https://github.com/falkensmz"><img src="https://i.ibb.co/NZbmyMk/smaze-stager.jpg" width=600 weigth=500 alt="smaze_stager"></a>
  <br>
  smaze_stager
  <br>
</h1>

<h4 align="center">smaze_stager : download & execute payload</h4>

## What is smaze_stager and how does it work?

smaze_stager is a simple download & execute payload. These type of payloads are designed to download more sophisticated malware that you specify , and execute it on the target system.

## Why would you use this?

This type of payload is much smaller than sophisticated reverse/bind shells or even malware. You can use this payload easilier in conjunction with social engineering. 

## How to use it?

 - Open the "smaze_stager.py" file with your favourite editor.
 ![example](https://user-images.githubusercontent.com/83426553/163732278-cc4efe4c-0542-44bb-99eb-18a9e1cc8928.PNG)
 
 - The only variables that you need to change are "link", "sleep_before" and "sleep_after".
 - Change the link to the link that hosts your virus/payload/malware. (Make sure that it is a direct mirror/download link and that it ends in .exe)
 - Change the "sleep_before" variable , if desired, to how many seconds you want smaze_stager to wait before it downloads the malware.
 - Change the "sleep_after" variable, if desired, to how many seconds you want smaze_stager to wait before it executes the malware.

## How to build it?

 - You can build smaze_stager as an executable (.exe) using something like <a href="https://pypi.org/project/pyinstaller/?msclkid=217044b9bef311ecbc0ff268d0619099"> pyinstaller</a> or <a href="https://pypi.org/project/pyarmor/?msclkid=1fbcf853bef311ec92869880b47e1ad0"> pyarmor </a>

## Disclaimer 

This program is made for educational purposes only. The developer of this payload is not responsible for any kind of misuse.
