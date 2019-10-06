#дынные
import requests
from bs4 import BeautifulSoup
from datetime import datetime
 
url = "https://www.cbr.ru/scripts/XML_daily.asp"
 
response = requests.get(url)


soup = BeautifulSoup(response.content, "lxml")


#ввод нужной суммы

CounUS = int(input("введите нужную сумму (в долларах): "))




#функция 1
def get_cource(id):
    valute = soup.find("valute", {"id": id})
    return f"{valute.value.text}"
usd = get_cource("R01235")

usd = usd.replace(",",".")

US = float(usd)


res1 =(US * CounUS) 

print("Ваша итоговая сумма: ", res1, "рублей")