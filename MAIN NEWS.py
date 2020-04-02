import requests
from bs4 import BeautifulSoup
url="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
data=soup.find_all('div',{'class': 'xrnccd F6Welf R7GTQ keNKEd j7vNaf'})
d=data[0]
filename="MAIN_NEWS.csv"
f=open(filename,"w", encoding="utf-8")
headers= "NEWS TITLE,NEWS TEXT,DATETIME,URL\n"
f.write(headers)
for d in data:
    title=d.h3.a.text

    subnews=d.find_all("div",{"class": "Da10Tb Rai5ob"})
    sub=subnews[0].span.text

    u= d.h3.a["href"]

    timet=d.find_all("div",{"class": "QmrVtf RD0gLb"})
    time=timet[0].time["datetime"]

    print(title.replace(",", "|") + "," + sub.replace(",", "|") + "," + time + "," +u + "\n")
    f.write(title.replace(",", "|") + "," + sub.replace(",", "|") + "," + time + "," +u + "\n")

f.close()
