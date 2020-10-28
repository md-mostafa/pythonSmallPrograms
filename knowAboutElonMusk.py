#use python to know about elon musk using beautifulsoup
import requests
from bs4 import BeautifulSoup

#link for extract html data
def getdata(url):
    r = requests.get(url)
    #print(r.text)
    return r.text

htmldata = getdata("https://en.wikipedia.org/wiki/Elon_Musk")
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''
for data in soup.find_all('p'):
    print(data.get_text())