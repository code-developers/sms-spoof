#!/usr/bin/env/python
import os
import random
import base64

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear()
print("This Tool Is Used To Send Anonyous Messages\n\n")
print("Enter The Details Of The Person You Want To Send Anonymous Message")
cc = input("\tEnter Country Code (Without +) : ")
if '+' in cc:
        tc = list(cc)
        tc.remove('+')
        cc = ''.join(tc)
        cc = cc.strip()
if len(cc) >= 4 or len(cc) < 1:
        print('\n\nInvalid Country Code..\n\t\tCountry Codes Are Generally 1-3 digits...\n')
        exit()
pn = input("Enter Phone Number(Without Country Code) : ")
if len(pn) <= 6:
        print('\n\nInvalid Phone Number..\n')
        banner()
        exit()
number = cc + pn
receiver = '+' + number
text = input("Enter Message to send : ")
os.system('''proxychains curl --request POST https://textbelt.com/text \
    --data-urlencode phone='{}' \
    --data-urlencode message='{}' \
    -d key=textbelt'''.format(number,text))
