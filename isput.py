from bs4 import BeautifulSoup
import requests
resource = requests.get('https://uaspeedfilms.club')
f = open("memchuk.txt","a+")
if resource.status_code == 200:
    soup = BeautifulSoup(resource.text,features="html.parser")
    name_list_soup = soup.find_all("strong",{"class":"shortnew-main-item-title"})
    year_list_soup = soup.find_all("strong", {"class": "Kp"})
    # res = soup_list[0].find("span")
    # print(res.text)
    nameList = []
    yearList = []
    for elName in name_list_soup :
        nameList.append(str(elName.text))
    lenList = len(nameList)
    print(lenList)
    l =[str(i) for i in range(0,lenList)]
    for i in range(0,lenList):
        str = l[i]+nameList[i]+"\n"
        f.write(str)
        print(l[i],")" , nameList[i],"|",)
