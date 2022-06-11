from bs4 import BeautifulSoup
import requests
resource = requests.get('https://coinmarketcap.com')
if resource.status_code == 200:
    soup = BeautifulSoup(resource.text,features="html.parser")
    soup_list = soup.find_all("div",{"class":"sc-131di3y-0 cLgOOr"})
    # res = soup_list[0].find("span")
    # print(res.text)
    c = len(name_list)
    for i in range(0,c):
        print(name_list[1].text, "-" , cost_list[1].text)