#this program is used for send a message to your loved once


import pywhatkit          # pywhatkit install using pip install pywhatkit then import
wno = input('whatsapp number: ')   
msg = input('Message: ')
hr = int(input('hour: '))
min = int(input('minutes: '))

pywhatkit.sendwhatmsg('+91'+ wno, msg, hr, min)
