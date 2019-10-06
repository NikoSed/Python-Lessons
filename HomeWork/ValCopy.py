#дынные
import requests
from bs4 import BeautifulSoup
from datetime import datetime
 
print("Вас приветствует Конвертатор валют")
 
url = "https://www.cbr.ru/scripts/XML_daily.asp"
 
response = requests.get(url)


soup = BeautifulSoup(response.content, "lxml")
def get_cource(id):
    valute = soup.find("valute", {"id": id})
    return f"{valute.value.text}"

#ввод нужной суммы
Vault = input("Выберите валюту: e - euro, u - dollar, ps - pound sterling ")



if Vault == "u":
    CounUS = int(input("введите нужную сумму (в долларах): "))




    #функция 1
    usd = get_cource("R01235")

    usd = usd.replace(",",".")

    US = float(usd)


    res1 =(US * CounUS) 

    print("Ваша итоговая сумма: ", res1, "рублей")

elif Vault == "ps":
    CounUS = int(input("введите нужную сумму (в фунтах-стерлингах): "))




    #функция 1
    usd = get_cource("R01035")

    usd = usd.replace(",",".")

    US = float(usd)


    res1 =(US * CounUS) 

    print("Ваша итоговая сумма: ", res1, "рублей")




elif Vault == "e":
    CounUS = int(input("введите нужную сумму (в евро): "))




    #функция 1
    usd = get_cource("R01239")

    usd = usd.replace(",",".")

    US = float(usd)


    res1 =(US * CounUS) 

    print("Ваша итоговая сумма: ", res1, "рублей")

