import requests
from bs4 import BeautifulSoup
import re

urlName = "https://jp.techcrunch.com"
url = requests.get(urlName)
soup = BeautifulSoup(url.content, "html.parser")

elems = soup.find_all("h2")

for elem in elems: 
  try:
    title = elem.text  
    print(title)
  except:
    pass
