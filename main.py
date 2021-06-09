import requests
from bs4 import BeautifulSoup

product=str(input("Enter the product name: "))
list=product.split(" ")
prod=("-".join(list)
#print(prod)
URL=f'https://www.amazon.com/'+{prod}+'/dp/B07M7V7TSK/ref=sr_1_1_sspa?dchild=1&keywords=mens+shoes&qid=1607059506&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFFVEc3U0Q5NUNSVlUmZW5jcnlwdGVkSWQ9QTAxOTU1MTZORFJaVVE5SjhMRFkmZW5jcnlwdGVkQWRJZD1BMDE5MjE3M09ZRzJLMEQ3R1FDSyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
print(URL)
headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
page=requests.get(URL,headers=headers)

soup=BeautifulSoup(page.content,'html.parser')
title=soup.find(id='productTitle').get_text().strip()
print(title)
