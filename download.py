
# 链接抓到txt保存
# =======================================================================

import requests
from bs4 import BeautifulSoup

urls=['https://cn.fashionbunker.com/new-arrivals?p={}'.format(str(i)) for i in range(1,19)]

with open('pic.txt','w') as f:
    for url in urls:
        html=requests.get(url)
        soup=BeautifulSoup(html.text,'lxml')
        imgs=soup.select('ul > li > a > img')
        h3s=soup.select('ul > li > a > h3')
        h2s = soup.select('ul > li > a > h2')
        prices=soup.select('span.regular-price > span.price')
        for img,h3,h2,price in zip(imgs,h3s,h2s,prices):
            f.write(img.get('src') + '\n')
            f.write(h3.text + '\n')
            f.write(h2.text + '\n')
            f.write(price.text[4:] + '\n')

# download https
# =======================================================================

import requests
import urllib.request
from bs4 import BeautifulSoup
#import ssl
import requests

#url = 'http://papers.xtremepapers.com/CIE/Cambridge%20IGCSE/Mathematics%20(0580)/0580_s03_qp_1.pdf'


#ssl._create_default_https_context = ssl._create_unverified_context
i=0
with open('pic.txt') as f:
    for line in f:
        i+=1
        if i%4==1:
            p1=line.strip()
        if i%4==3:
            p2 = line.strip()
        if i % 4 == 0:
            r = requests.get(p1)
            with open('./imgs/' + p2+'.jpg', 'wb') as outfile:
                outfile.write(r.content)
