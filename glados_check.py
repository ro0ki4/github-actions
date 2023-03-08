import requests
import random
import time
import os

url = "https://glados.rocks/api/user/checkin"

payload = "{\"token\":\"glados.network\"}"
headers = {
  'authority': 'glados.rocks',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'zh-CN,zh;q=0.9',
  'authorization': '82302881659233442411435473100087-900-1440',
  'content-type': 'application/json;charset=UTF-8',
  'cookie': 'koa:sess=eyJ1c2VySWQiOjMyMTQ0LCJfZXhwaXJlIjoxNjk5MjM2NTAwODMxLCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=ceIesg5iKKrSuu8WzxkhOpPkSFU; Cookie=enabled; Cookie.sig=lbtpENsrE0x6riM8PFTvoh9nepc; _ga=GA1.2.780350391.1673316798; _gid=GA1.2.1407532535.1673316798',
  'dnt': '1',
  'origin': 'https://glados.rocks',
  'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

timeSecond = random.randint(1,59)
timeMin = random.randint(0,1)
# timeMin = 0
time.sleep(timeSecond+timeMin*60)

response = requests.request("POST", url, headers=headers, data=payload)


if (response.text.find("Checkin! Get 1 Day") != -1):
  print("success")
elif (response.text.find("Please Try Tomorrow") != -1):
  print("success")
else:
  print("fail")



  




