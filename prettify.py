import requests
from bs4 import BeautifulSoup
url="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
data=soup.find_all('div',{'class': 'xrnccd F6Welf R7GTQ keNKEd j7vNaf'})
print(BeautifulSoup.prettify(data[0]))#will give the html structure of the page