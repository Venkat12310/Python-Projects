import pywhatkit
wno = input('whatsapp number: ')
msg = input('Message: ')
hr = int(input('hour: '))
min = int(input('minutes: '))

pywhatkit.sendwhatmsg('+91'+ wno, msg, hr, min)