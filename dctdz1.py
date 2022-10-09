import requests, os, sys
from datetime import time
from sys import exit
import datetime
import time
from time import sleep
os.system('pip install colorama')
from colorama import Fore
os.system('clear')
print("\033[1;32m╔═══════════════════════════════════════════════════════════════════════════╗\r")
print("\033[0;34m                         Copyright ©Trần Đăng Khoa                           ") 
\033[1;32m     _                   \033[0;37m  __| | ___   __ _ _ __  \033[1;93m / _` |/ _ \ / _` | '_ \ ")
print("\033[1;32m| (_| | (_) | (_| | | | |\033[0;37m \__,_|\___/ \__,_|_| |_| \033[1;93m      _     _            ")
print("\033[1;32m  ___| |__ (_) ___ _ __  \033[0;37m / __| '_ \| |/ _ \ '_ \ \033[1;93m| (__| | | | |  __/ | | |")
print("\033[1;32m \___|_| |_|_|\___|_| |_|\033[0;37m _   _                       \033[1;93m| |_| |__  _   _  __ _ _ __  ")
print("\033[1;32m| __| '_ \| | | |/ _` | '_ \ \033[0;37m| |_| | | | |_| | (_| | | | |\033[1;93m \__|_| |_|\__,_|\__,_|_| |_|                         ")
print    ( "\033[1;32m╚════════════════════════════════════════════════════════════════════════════╝")
cookie=input(Fore.GREEN+"Nhập Cookie: "+Fore.YELLOW)
linkfb=input(Fore.GREEN+"Nhập Link Facebook: "+Fore.YELLOW)
tinnhan=input(Fore.GREEN+"Nhập Tin Nhắn: "+Fore.YELLOW)
solan=int(input(Fore.GREEN+"Nhập Số Lần Spam: "+Fore.YELLOW))
delay=int(input(Fore.GREEN+"Nhập Delay: "+Fore.YELLOW))
head={
   'Host':'id.traodoisub.com',
   'content-length':'54',
   'sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
   'accept':'application/json, text/javascript, */*; q=0.01',
   'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
   'x-requested-with':'XMLHttpRequest',
   'sec-ch-ua-mobile':'?1',
   'user-agent':'Mozilla/5.0 (Linux; Android 11; vivo 1906) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
   'sec-ch-ua-platform':'"Android"',
   'origin':'https://id.traodoisub.com',
   'sec-fetch-site':'same-origin',
   'sec-fetch-mode':'cors',
   'sec-fetch-dest':'empty',
   'referer':'https://id.traodoisub.com/',
   'cookie':'cf_clearance=z1jER0ZpxOgJR09akK8mhmHGWP1dg8.AV8p7xOxQOsc-1661855178-0-150'
}
data=(f"link={linkfb}")
get=requests.post("https://id.traodoisub.com/api.php",headers=head,data=data).text
a=get.find("error")
sleep(3)
tds=requests.post("https://id.traodoisub.com/api.php",headers=head,data=data)
if a>=0:
 check=tds.json()['error']
 print(Fore.GREEN+"error:"+Fore.RED,check)
else:
 id=tds.json()['id']
headfb={
   'Host':'mbasic.facebook.com',
   'upgrade-insecure-requests':'1',
   'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5057.107 Safari/537.36',
   'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
   'sec-fetch-site':'cross-site',
   'sec-fetch-mode':'navigate',
   'sec-fetch-user':'?1',
   'sec-fetch-dest':'document',
   'cookie':cookie,
  }
headers={
   'Host':'mbasic.facebook.com',
   'content-length':'289',
   'cache-control':'max-age=0',
   'sec-ch-ua':'"Chromium";v="105", "Not)A;Brand";v="8"',
   'sec-ch-ua-mobile':'?1',
   'sec-ch-ua-platform':'"Android"',
   'upgrade-insecure-requests':'1',
   'user-agent':'Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4990.82 Safari/537.36',
   'origin':'https://mbasic.facebook.com',
   'content-type':'application/x-www-form-urlencoded',
   'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
   'sec-fetch-site':'same-origin',
   'sec-fetch-mode':'navigate',
   'sec-fetch-user':'?1',
   'sec-fetch-dest':'document',
   'referer':'https://www.facebook.com',
   'cookie':cookie,
}
home=requests.get('https://mbasic.facebook.com',headers=headfb).text
checkck=home.find('Đăng nhập hoặc đăng ký')
if checkck==-1:
 fb=requests.get('https://mbasic.facebook.com/profile.php',headers=headfb).text.split("Chỉnh sửa trang cá nhân")[0]
 id_fb=fb.split("/profile.php?lst=")[1].split("%")[0]
 ten_fb=fb.split('title>')[1].split('<')[0]
 print(Fore.GREEN+f"Bạn Đang Spam Tin Nhắn Bằng Tài Khoản:{Fore.BLUE}{ten_fb}{Fore.GREEN} & Id Là:{Fore.BLUE}{id_fb}")
 a=requests.get(f"https://mbasic.facebook.com/messages/read/?fbid={id}",headers=headfb).text.split('/messages/read/?')[1].split('"')[0].replace('amp;','')
 b=requests.get(f"https://mbasic.facebook.com/messages/read/?fbid={id}",headers=headfb).text.split("fb_dtsg")[1].split('value="')[1].split('"')[0]
 c=requests.get(f"https://mbasic.facebook.com/messages/read/?fbid={id}",headers=headfb).text.split('fb_dtsg')[1].split('jazoes')[1].split('value="')[1].split('"')[0]
 d=requests.get(f"https://mbasic.facebook.com/messages/read/?fbid={id}",headers=headfb).text.split('fb_dtsg')[1].split('tids')[1].split('value="')[1].split('"')[0]
 e=requests.get(f"https://mbasic.facebook.com/messages/read/?fbid={id}",headers=headfb).text.split('fb_dtsg')[1].split('wwwupp')[1].split('value="')[1].split('"')[0]
 f=requests.get(f"https://mbasic.facebook.com/messages/read/?fbid={id}",headers=headfb).text.split('fb_dtsg')[1].split('name="ids[')[1].split('"')[0]
 g=requests.get(f"https://mbasic.facebook.com/messages/read/?fbid={id}",headers=headfb).text.split('fb_dtsg')[1].split('csid')[1].split('value="')[1].split('"')[0]
 data=(f"fb_dtsg={b}&jazoest={c}&body={tinnhan}&send=G%E1%BB%ADi&tids={d}&wwwupp={e}&ids[{f}={id}&referrer=&ctype=&cver=legacy&csid={g}")
 for i in range(1,solan+1):
  requests.post(f"https://mbasic.facebook.com/messages/send/?{a}",data=data,headers=headers)
  print(f"{Fore.GREEN}Đã Gửi Thành Công {Fore.YELLOW}{i}{Fore.GREEN} Số Tin Nhắn{Fore.YELLOW} {tinnhan}{Fore.GREEN} cho {Fore.YELLOW}{id}")
  for i in range(delay,-1,-1):
        print('Vui Lòng Chờ '+str(i)+' Giây ',end=(    '\r'))
        print(' ',end='')
        time.sleep(1)
else:
  print(Fore.RED+"Cookie Die !!")