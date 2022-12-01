import requests
from bs4 import BeautifulSoup
import socket
 
user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
url = 'https://www.youtube.com'
reqs = requests.get(url, headers=user_agent)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    urls.append(link.get('href'))

clean_urls = [item for item in urls if 'https' in item]

print("##########################################")
print("#                                        #")
print("#            LINKS ENCONTRADOS:          #")
print("#                                        #")
print("##########################################")


for x in clean_urls:
    print(f'{x}')

print("##########################################")
print("#                                        #")
print("#            IPS DAS URL:                #")
print("#                                        #")
print("##########################################")


for x in clean_urls:
        try:
            ip = socket.gethostbyname(x[8:].split('/')[0])
            print(f"{x} -------> {ip}")
        except:
            pass
