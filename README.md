# GETXE

A basic tool to scrap the exchange rate of currencies on a daily basis.
If the exchange rate verifies a condition, an email is sent to the specified email addresses.
Automator® on OS X allows to launch the script in the background when the user logs in.  

> BeautifulSoup + schedule + smtplib

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