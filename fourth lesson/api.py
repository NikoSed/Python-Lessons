import requests
from bs4 import BeautifulSoup
from datetime import datetime
 
url = "https://www.cbr.ru/scripts/XML_daily.asp"
 
response = requests.get(url)
 
#print(response.content)

soup = BeautifulSoup(response.content, "lxml")

def get_cource(id):
    valute = soup.find("valute", {"id": id})
    return f"За {valute.nominal.text} {valute.nominal.next_sibling.text} дают {valute.value.text} рублей"
usd = get_cource("R01235")

valutes = soup.find_all("valute")

for x in valutes:
    print(get_cource(x['id']))