from bs4 import BeautifulSoup
import urllib.request
import socket

links = []
ips = []
headers = {'User-Agent': 'Mozila/5.0'}
html_page = urllib.request.urlopen("https://datagy.io/", headers=headers)
soup = BeautifulSoup(html_page, "html.parser")
for link in soup.findAll('a'):
    links.append(link.get('href'))


new_links = [item for item in links if 'htt' in item]

print("##########################################")
print("#                                        #")
print("#            LINKS ENCONTRADOS:          #")
print("#                                        #")
print("##########################################")

for x in new_links:
   print(f"{x}")



print("##########################################")
print("#                                        #")
print("#            IPS DOS MESMOS:             #")
print("#                                        #")
print("##########################################")

for x in new_links:
    try:
        ip = socket.gethostbyname(x[7:])
        print(ip)
    except:
        pass
