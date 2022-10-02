import requests
import random
code = input("your dsc.gg code >> ")
i = int(input("how many views >> "))


x = 1


headers = {
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }

while (i > x):
  requests.get(f"https://dsc.gg/{code}?ref=homepage", headers=headers)
  print("sent 1 view")
  i += 1
  
