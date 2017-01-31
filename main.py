import vk
import datetime
import time
import serial
import pyowm

def internet_on():
    try:
        urllib2.urlopen('http://vk.com', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

def searchForUser(ID):
    user = api.users.get(user_ids = ID)
    user = user[0]
    return user['first_name'] + ' ' + user['last_name'] + '\n'

def checkMessages(message_list):
    count_msg, count_form_a = 0 , 0

    IDS = []
    for message in message_list:
        if type(message) is int:
            continue
        if message['read_state'] == 0:
            count_msg +=1
            if message['uid'] == 200267227:
                count_form_a +=1
            if 'chat_id' not in message and str(message['uid']) not in IDS:
                IDS.append(str(message['uid']))


    text = '%d(%d)msg' % (count_msg, count_form_a)
    return text

def firstZero(num):
    if num < 10 :
        return '0'+str(num)
    else:
        return str(num)




##########
##########
session = vk.Session(access_token = 'eba55bc9b524ce80e710a904f7b3eeae10113381d0d5a895c3bf5efd463f93ae746a18a2cdaf5106046cb')
api = vk.API(session, lang = 'en')  

owm = pyowm.OWM('1bc7daa3d4206a5608fa3cc8e4abc03d')

ser = serial.Serial('COM4')   # open serial port

observation = owm.weather_at_place('Minsk,BY')
w = observation.get_weather()


i = 0
temp = ''

while True:
    now_time = datetime.datetime.now() 
    message = api.messages.get(time_offset = 0)
    if len(message) != 1 and message[1]['read_state'] == 0:
        ser.write('You have %s\n' % checkMessages(message)) 
    else:
        ser.write('No messages\n')
    if i%1440 :
         temp = w.get_temperature('celsius')['temp']
         i = 0
    ser.write(b'%s\n' % temp)
    ser.write('%s\n' % firstZero(now_time.hour))
    ser.write('%s\n' % firstZero(now_time.minute))
    
    i+=1
    time.sleep(5)
#access_token = eba55bc9b524ce80e710a904f7b3eeae10113381d0d5a895c3bf5efd463f93ae746a18a2cdaf5106046cb&expires_in=0&user_id=157769959