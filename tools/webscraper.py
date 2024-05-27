import requests
from bs4 import BeautifulSoup

res = requests.get("https://freevpn.me/accounts")
soup = BeautifulSoup(res.content,'html.parser')

data = soup.find_all('div',{'class':'span4'})[0]

for datas in data:
        print(datas.get_text())


#print(soup.get_text())
print("status code :\t", res.status_code)

