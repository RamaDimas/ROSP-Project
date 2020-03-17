from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep
from datetime import datetime
import json, re, sys, os
with open('dogeclickbot.json', 'r') as (myfile):
 data = myfile.read()
rcm = json.loads(data)
wl = (rcm['Wallet'])
try:
 import requests
 from bs4 import BeautifulSoup
except:
 print(t + ' \x1b[1;31mHmmm Sepertinya Modul Requests Dan Bs4 Belum Terinstall\n? \x1b[1;31mTo install Please Type pip install requests and pip install bs4')
 sys.exit()
if not os.path.exists('session'):
 os.makedirs('session')
c = requests.Session()
ua = {'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'}
api_id = 739027
api_hash = '2645168f6e11a9daf55f4d589b03541a'
phone_number = sys.argv[1]
client = TelegramClient('session/' + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
 try:
  client.send_code_request(phone_number)
  me = client.sign_in(phone_number, input('\n\x1b[1;0mEnter Your Code : '))
 except SessionPasswordNeededError:
  passw = input('\x1b[1;0mYour 2fa Password : ')
  me = client.start(phone_number, passw)
myself = client.get_me()
nicke = ('[' + myself.first_name + ']')
try:
 channel_entity = client.get_entity('@Dogecoin_click_bot')
 channel_username = '@Dogecoin_click_bot'
 client.send_message(entity=channel_entity, message='/cancel')
 client.send_message(entity=channel_entity, message='/start')
 for i in range(99999999):
  nicke = nicke
  ttt = (datetime.now().strftime('%D %H:%M:%S'))
  tt = (datetime.now().strftime('%H:%M:%S'))
  t = ('\x1b[1;39m[' + tt + ']')
  client.send_message(entity=channel_entity, message='Balance')
  sleep(0.5)
  posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
  if posts.messages[0].message.find('Available') !=-1:
    sleep(0.5)
    posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
    messageaa = posts.messages[0].message
    messageaa = re.findall('([\\d.]*\\d+)', messageaa)
    blc = float(messageaa[0])
    cm = '% 6.8f' % blc
    def tunggu(x):
     sys.stdout.write('\r')
     sys.stdout.write('                                                               ')
     for remaining in range(x, 0, -1):
      sys.stdout.write('\r')
      sys.stdout.write(t + '\x1b[1;0m{:2d} '.format(remaining) + '\x1b[1;33mBalance ' + cm + ' DOGE')
      sys.stdout.flush()
      sleep(1)
  sys.stdout.write('\r')
  sys.stdout.write('                                                              ')
  sys.stdout.write('\r')
  sys.stdout.write(t + '\x1b[1;33m Balance ' + cm + ' DOGE')
  sleep(0.5)
  sys.stdout.flush()
  client.send_message(entity=channel_entity, message='Visit sites')
  sleep(0.5)
  posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
  def logg():
    nick = nicke
    dblc = cm + " DOGE"
    file_bio = open("dogeclickbot.log", "r+")
    dglog = file_bio.read()
    dglog = " \n" + ttt + "\r{}{}".format(nick,dblc)
    file_bio.write(dglog)
    file_bio.close()
  if posts.messages[0].message.find('Sorry, there are no new ads available') != -1:
   x = float(11)
   if blc > x:
    client.send_message(entity=channel_entity, message='Withdraw')
    client.send_message(entity=channel_entity, message=wl)
    client.send_message(entity=channel_entity, message='11')
    client.send_message(entity=channel_entity, message="Confirm")
    sys.exit()
   else:
    logg()
    sys.exit()
  else:
   try:
    url = posts.messages[0].reply_markup.rows[0].buttons[0].url
    sys.stdout.write('\r')
    sys.stdout.write(t + '\x1b[1;33m Balance ' + cm + ' DOGE')
    sys.stdout.flush()
    id = posts.messages[0].id
    r = c.get(url, headers=ua, timeout=15, allow_redirects=True)
    soup = BeautifulSoup(r.content, 'html.parser')
    if (soup.find('div', class_='g-recaptcha')) is None and (soup.find('div', id='headbar')) is None:
     sleep(0.5)
     posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
     message = posts.messages[0].message
     if posts.messages[0].message.find('You must stay') != -1 or posts.messages[0].message.find('Please stay on') != -1:
      sec = re.findall('([\\d.]*\\d+)', message)
      tunggu(int(sec[0]))
      sleep(0.5)
      posts = client(GetHistoryRequest(peer=channel_entity, limit=2, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
      messageres = posts.messages[1].message
      messageres = re.findall('([\\d.]*\\d+)', messageres)
      messageres = messageres[0]
      sleep(0.5)
      sys.stdout.write('\r')
      sys.stdout.write(t + '\x1b[1;32m Success Claim ' + messageres + '00000 DOGE      \n')
      sys.stdout.write(t + '\x1b[1;33m Balance ' + cm + ' DOGE')
      sys.stdout.flush()
    else:
     if (soup.find('div', id='headbar')) is not None:
      for dat in soup.find_all('div', class_='container-fluid'):
       code = dat.get('data-code')
       timer = dat.get('data-timer')
       tokena = dat.get('data-token')
       tunggu(int(timer))
       r = c.post('https://dogeclick.com/reward', data={'code':code,  'token':tokena}, headers=ua, timeout=60, allow_redirects=True)
       js = json.loads(r.text)
       sys.stdout.write('\r')
       sys.stdout.write(t + ' \x1b[1;32mSuccess Claim ' + js['reward'] + '00000 DOGE\n')
       sys.stdout.write(t + '\x1b[1;33m Balance ' + cm + ' DOGE')
       sys.stdout.flush()
     else:
      sys.stdout.write('\r')
      sys.stdout.write('                                                              ')
      sys.stdout.write('\r')
      sys.stdout.write(t + '\x1b[1;33m Balance ' + cm + ' DOGE')
      sys.stdout.flush()
      sleep(15)
      client(GetBotCallbackAnswerRequest(channel_username,id,data=posts.messages[0].reply_markup.rows[1].buttons[1].data))
      sleep(0.5)
      sys.stdout.write('\r')
      sys.stdout.write(t + '\x1b[1;33m Balance ' + cm + ' DOGE')
      sys.stdout.flush()
   except:
    sleep(0.5)
    posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
    message = posts.messages[0].message
    if posts.messages[0].message.find('You must stay') != -1 or posts.messages[0].message.find('Please stay on') != -1:
     sec = re.findall('([\\d.]*\\d+)', message)
     tunggu(int(sec[0]))
     sleep(0.5)
     posts = client(GetHistoryRequest(peer=channel_entity, limit=2, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
     messageres = posts.messages[1].message
     messageres = re.findall('([\\d.]*\\d+)', messageres)
     messageres = messageres[0]
     sleep(0.5)
     sys.stdout.write('\r')
     sys.stdout.write(t + ' \x1b[1;32mSuccess Claim ' + messageres + '00000 DOGE\n')
     sys.stdout.write(t + '\x1b[1;33m Balance ' + cm + ' DOGE')
finally:
 client.disconnect()
