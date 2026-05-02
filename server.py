from pickle import TRUE
from pyexpat.errors import messages
from cgi import test
from email import message
from operator import mod
from random import sample
import socket
import base64
from configobj import ConfigObj #pip install configobj
import pandas as pd
import csv
import time
#================================================
#function for test
def tester():
    print("Hello from tako")
    print("Morbillion dollars ticket")
#================================================
#function to encode to base64
def encodeBase64(message_in):
    message_bytes = message_in.encode()
    base64_bytes = base64.b64encode(message_bytes)
    base64_string = base64_bytes.decode()
    return base64_string
#================================================
#function to decode base 64
def decodeBase64(base64_string):
  base64_bytes = base64_string.encode()
  message_bytes = base64.b64decode(base64_bytes)
  message_in = message_bytes.decode()
  return message_in
#================================================
#function for request secret number
def requestSecretNum(input):
    parts = input.split(':')
    if((len(parts)==4 and parts[1] == 'request secret number')):
        try:
            x = int(parts[2])
            y = int(parts[3])
        except:
            print('Error! : your pattern is invalid')
#================================================
#function for send encrypted secret num back to client
def Cipher(e,n):
    n = int(n)
    e = int(e)
    s = 6 + 3 + 0 + 9 + 6 + 5 + 0 + 0 + 3 + 1
    s = 33
    Cipher = pow(s,e,n) #Cipher Text = secret^e mod n
    Cipher_text = 'Encrypted Secret Number:' + str(Cipher)
    data.sendto(Cipher_text.encode(),(HOST,PORT)) #send message back to client
#================================================
def checkSecretNum(in_num):
    #secret number = 33
    in_num = int(in_num)
    SecrectNum = 6 + 3 + 0 + 9 + 6 + 5 + 0 + 0 + 3 + 1
    print(" 60 : Secret Number is : " + str(SecrectNum) + " and we compare it to " + str(in_num))
    if in_num == SecrectNum:
        return True
    else:
        return False
#================================================
#check username, password is match
def CheckUserdata(username, password):
    oki = 0
    if username in users:
        print(" 70 : Chek User name is OK!")
        oki = oki +1
    if password in psswd:
        print(" 73 : Check password is OK!")
        oki = oki +1
    if oki == 2:
        return 3
#================================================
#function for quit
def Quit():
    messenger = 'Session is closed.'
    messenger.sendto(message.encode(),(HOST,PORT))
    s.close()
#================================================
def TokenAuth(toke):
    try:
        tparts = decodeBase64(toke)
        tparts = tparts.split('.')
        if(CheckUserdata(tparts[0],tparts[1]) == 3):
            return True
        else:
            return False
    except: 
        return False
#====================!!!============================================================================
#=================== main ==========================================================================
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..,,,,,,,,,,,,,,,,,,,,,,.
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..            .. ...  .               .,,,,,,,,,,,,,,,,,,,,.,,.
#,,,,,,,,*,,,,,,,,,,,,,,,,,,,,,,,..  .,*/(#####%%%###(*,   ..                    ,,,,,,,,,,,,.....,.
#,,,,,,,***,,,,,,,,,,,,,,,,,,,,.  ,/(#%%%%%%%%%%%%%%%%%%%%#(*..                     .,,,,,,,,,..,.,.
#,,,,,,,,**,,,,,,,,,,,,,,,,,,. ,(##%%%%%%%%%%%#%%%%%%%%%%%%%%%#/.                     ..,,,,,,,,,,,,
#,,,,,,,,**,,,,,,,,,,,,,,,,..,(##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*                     ..,,,,,,,,,,
#,,,,,,,,**,,,,,,,,,,,,,,,..*###%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(,  .                  ..,,,,,,,.
#,,.,,,,,**,,,,,,,,,,,,,..,(##((/*,,,.....    ...,,/((#%%%%%%%%%%%%%%/. ..                  ..,,,,,.
#,,.,,,.,**,,,,,,,,,,,,,.*/*....,*,*/////////**//****,,.  .*(%%%%%%%%#*  .                   ..,,,,.
#,.,,,,.,***,,,,,,,,,,,.....*/*(#**(((((((((((((((((**(#*,**.  ./#%%#%(.                      .,,,,.
#...,,,.,***,,,,,,,,,,. ,/(((*(%(,*((((((((((((((((/,(%#*,/((((*...,((/.                       ..,,.
#,..,,,.,***,,,,,,,,,. ,((((,/%%(./((#((#((((((##((,*%%#/*/((((((/,.....                   .    .,, 
#,..,,,.,***,,,,,,,,,.,((((**#%%(./(#((##((//(##((*,(%%%(.*((####((((*,.                 ....    .,.
#...,,,.,***,,,,,,,,,./((#(**#%%#.*(##(##((**((((/,*#%%%%/.*((#######((.                    .    .,.
#...,,,.,**,,,,,,,,,..((#((*/#%%%/,(((((((*,,/(((/,/#%%%%%(.*((######((.                         ,,.
#...,,,,,**,,,,,,,,,. /((((/*#%%%%,*((((((,//,(((*,(%%%%%%%/.*((####((/.                        .,,.
#,,,,,,,,,*,,,,,,,,,.  *(((/,(%%%#*./((((/./#/,/(*.(%%%%%%%%/.*(((((((*                         .,,.
#........,,,.........  ,,,.,.,/(##(*,*(((/,/,,,,/*.(%#%%%%%%%(.,/(((((,                         .,,.
#,,,,,,,,,,,,,,,,,,,,. /(,/#/*/#%%%#/.,(((,*#%%#*,.(###((/*,*#%/.,/((/.                         .,,.
#,,,,,,,,,,,,,,,,,,,,. ,#/,.,*****/#%#(,,*(*/#####* /%%%###(#%%%%(,.*,                          .,,.
#,,,,,,,,,,,,,,,,,,,,. .#####/. ./#%%%%%#(/*,*#%#/#/,,////*/####%%%#(.                         .,,,.
#,,,,,,,,,,,,,,,,,,,,. .#%#(#(//.  *(#%%%%%%%%#, ..,**,**,/#(#######(.                         .,,,.
#,,,,,,,,,,,,,,,,,,,,  ,(.   .,/(######%%%%%%%#/*.,*,(%#############*                          .,,,.
#,,,,,,,,,,,,,,,,,,,, .(###/(((##%#####%%%%%%%%%%%##(/*,,,*(#######(,                         .,,,,.
#,,,,,,,,,,,,,,,,,,,. /###(#(/#####*,,(%%%%%%%%%%######*((/########(.                         ,,,,,.
#,,,,,,,,,,,,,,,,,,, .(##/(#/(###%*.#%%%%%%%%%%%######(/%#/########/                         .,,,,*,
##,,,,,,,,,,,,,,,,,,,. ,####/(###%%%%%%%%%%%%%%%%%%####((%(/########,                         .,,,,*.
#,,,,,,,,,,,,,,,,,,,,  ,(##/(%%%%%((/(#%##((/*,,,*(%##((%/(########,                         ,,,,,*.
#,,,,,,,,,,,,,,,,,,,,,. ./#(#%%%/.*//////////////*,/#%(#%/(%######/                         .,,,,**.
#,,,,,,,,,,,,,,,,,,,,,,,. .,*#%%#,*///////////////,/%%(%#(#######(.                         .,,,,**.
#,,,,,,,,,,,,,,,,,,,,,,,,,.  .(%%%(///////////((*,(%%#/%(/(###/*,,     .                    .,,,,**.
#...............,,,,,,,,.,,,.. ,#%%%%%#(//////#%%%%%##%#(/*,*,.,,.                           .,,,,.
#...............,,,,,,,,.,,,...... ,#%#%%%%%%%%%%%%%%#/*,,,**/(((/.                          . .,,,.
#...............,,,,,,,,.,,,........ *#%%%%%%%##(/,,,******((#(#(.                             .,,.
#...............,,,,,,,,.,,,..........  .,,.  . ..,,*****/(//(((/..                             .,.
#...............,,,,,,,,.,,,...........................,******(((((/,                              ..
#...............,,,,,,,,.,,,...........................,****////////.                               
#...,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..,,,,,,,,,,,,,,,,,,,,,,..
#=====================!!!===========================================================================
#attributes
conf = ConfigObj('server.config')
HOST = 'localhost'
PORT = int(conf['server_port'])
secrets_key = conf['secret_key']
#open .csv file to read user data
users = []
psswd = []
token = "blank"
with open('user_pass.csv')as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    for row in datareader:
        users.append(row[0])
        psswd.append(row[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))

#receive message from client
s.listen()
while True:
    try:
        data , address = s.accept() #<username>:<password> : receive from client
        attempt = 0
        while attempt <= 3:
            input = data.recv(1024)
            input = input.decode()
            input = input.split(':') #user:pass
            input_user = input[0]
            input_password = input[1]
            attempt = attempt + 1
            if(CheckUserdata(input_user, input_password) == 3):
                token = encodeBase64(input_user+"."+input_password+"."+secrets_key)
                hermes = "token:" + token
                data.sendto(hermes.encode(),address)
                attempt = 999
            if attempt == 3 and CheckUserdata(input_user, input_password) != 3:
                warning = 'Invalid username or password ' + str(attempt) + '/3 times'
                print('173 : to Client --> Invalid username or password ' + str(attempt) + '/3 times')
                data.sendto(warning.encode(),address)
                warning = 'Connection refused!! you’ve exceeded maximum number of attempts'
                print("176 : to Client --> Connection refused!! you’ve exceeded maximum number of attempts")
                data.sendto(warning.encode(),address)
                s.close()
                break
            if attempt != 3 and CheckUserdata(input_user, input_password) != 3:
                print("181 : User information is match with .csv : " + str(CheckUserdata(input_user, input_password) == 3))
                print("182 : to Client --> Invalid username or password " + str(attempt) + "/3 times")
                send = 'Invalid username or password ' + str(attempt) + '/3 times'
                data.sendto(send.encode(),address)
        #end auth
        
        attempt2 = 0
       

        while True:
            input = data.recv(1024)
            input = input.decode()
            aria = input.split(':') #user:pass
            print(input)
            print(aria)
            #sender = 'meow'
            #data.sendto(sender.encode(),address)
            attempt2 = attempt2 + 1
            #---------------------
            #   Authentication
            #---------------------
            Token_pass = False

            if(len(aria) <= 1):
                authen_status = 'Authenticated :false'
                print('206 : to client -->' + authen_status)
                data.sendto(authen_status.encode(),address)
                Token_pass = False
            if(len(aria) > 1):
                #attempt max
                if attempt2 == 3 and TokenAuth(aria[0]) == False:
                    authen_status9 = 'Connection refused!! you’ve provided wrong tokens '+ str(attempt2) + ' times in a row'
                    print('213 : to client -->' + authen_status9)
                    data.sendto(authen_status9.encode(),address)
                    Token_pass = False
                    s.close()
                    break
                if attempt2 < 3 and TokenAuth(aria[0]) == False:
                    print("    : this is " + str(attempt2) + " attempts")
                    authen_status8 = 'Authenticated :false'
                    print('221 : to client -->' + authen_status8)
                    data.sendto(authen_status8.encode(),address)
                    Token_pass = False
                if(TokenAuth(aria[0]) == True):
                    attempt2 = 999
                    authen_status = 'Authenticated : true'
                    print('227 : to client -->' + authen_status)
                    data.sendto(authen_status.encode(),address)
                    Token_pass = TRUE
            #---------------------
            #   message
            #---------------------
            #Case Request Secret Number : NTYwOTYxMDc2MC4wNzYwLmtleQ==:request secret number:5:221
            # 0token : 1message : 2e : 3n (len == 4)
            if(TokenAuth(aria[0]) == True):
                if((len(aria)==4) and aria[1] == 'request secret number'):
                        if(TokenAuth(aria[0]) == True):
                            print('238 : request secret number')
                            Cipher(aria[2],aria[3])
                            print('240 : called Cipher, we are going even deeper.')
                #Case Check Secret Number : NTYwOTYxMDc2MC4wNzYwLmtleQ==:check secret number:40
                if((len(aria)==3) and aria[1] == 'check secret number'):
                    print('243 : check secret number')
                    print(checkSecretNum(aria[2]))
                    if(checkSecretNum(aria[2]) ==  True):
                        text_chs = 'Secret Number Verification: true'
                        data.sendto(text_chs.encode(),address)
                    else:
                        text_chs = 'Secret Number Verification:false'
                        data.sendto(text_chs.encode(),address)
                #Case Quit : NTYwOTYxMDc2MC4wNzYwLmtleQ==:quit
                if((len(aria)==2) and aria[1] == 'quit'):
                    print('253 : quitting')
                    text_quit = 'Session is closed.'
                    data.sendto(text_quit.encode(),address)
                    s.close()
                    break

    finally:
        print("260 : at finally, terminate the server, oyasumi.")
        s.close()
    break