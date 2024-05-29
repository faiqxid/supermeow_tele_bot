import requests
import time
import random

param_claim = input('Masukan Data Parameter example "telegram=68xxxx" : ')
headers = {
    'accept': 'application/json; indent=2',
    'accept-language': 'id-ID,id;q=0.9,en-ID;q=0.8,en;q=0.7,en-US;q=0.6',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://lfg.supermeow.vip',
    'priority': 'u=1, i',
    'referer': 'https://lfg.supermeow.vip/',
    'sec-ch-ua': '""',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; Redmi Note 8 Build/TQ3A.230901.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36',
}

url_claim = 'https://api.supermeow.vip/meow/claim?'+param_claim

while True:
    response = requests.post(url_claim, headers=headers).json()
    balance = response['balance']
    print('Your Balance ', balance)
    rand_delay = random.randint(3700, 4000)
    delay = rand_delay
    for i in range(delay, 0, -1):
        minutes, seconds = divmod(i, 60)
        hours, minutes = divmod(minutes, 60)
        print(f"Next Claim In : {hours:02d}:{minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(1)