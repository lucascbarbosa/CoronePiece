from bs4 import BeautifulSoup
from urllib.request import Request,urlopen,urlretrieve
import csv
import requests
from PIL import Image
for i in range(1,925):
    
    url = 'https://onepiece.fandom.com/wiki/Episode_%d?file=Episode_%d.png'%(i,i)
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content)
    imgs = soup.findAll('img')
    for img in imgs:
        img_url = img['src']
        print(img_url)
        urlretrieve(img_url, "imgs/%d.jpg"%i)
        img = Image.open("imgs/%d.jpg"%i)
        print(img.size)
        if img.size > (250,250):
            print('foo')
            break
        else:
            pass
        
        