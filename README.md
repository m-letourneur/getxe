# README

## Config file
Write a config.py in the root directory that contains:

>EMAIL = 'your gmail email'

>PASSWORD = 'your gmail password'

Be sure to leave the config.py file in the .gitignore 

You can setup a shell script running this code, and make Automator® run the script when you login on the computer.

## Shell script

Modify the path to the repo directory in the file:
> run_getxe.sh

## Automator®

- Open Automator®

- Create a new "application"

- Select "Run Shell Script" in "Actions"

- Copy/paste run_getxe script into the text box

- Save as an application 

- Open System Preferences/Users & Groups

- Select Login Items tab

- Add the application you just created by clicking on "+"

- Tick or untick the box to run the app when you log in to your session