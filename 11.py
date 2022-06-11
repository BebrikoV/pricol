from bs4 import BeautifulSoup
import requests
resource = requests.get('https://coinmarketcap.com')
if resource.status_code == 200:
    soup = BeautifulSoup(resource.text,features="html.parser")
    soup_list = soup.find_all("a",{"href":"/currencies/bitcoin/markets/"})
    res = soup_list[0].find("span")
    print(res.text)