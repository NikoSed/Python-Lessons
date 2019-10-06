import requests
from bs4 import BeautifulSoup

def temp(html):
    return html.find("span",{"class":"temp__value"}).text
def opt(html):
    return html.find("div",{"link__condition"}).text
def gor(html):
    return html.find("h1",{"title title_level_1 header-title__title"}).text
def timesun(html):
    return html.find("dd",{"sunrise-sunset__value"}).text
def timenigh(html):
    return html.find("dl",{"sunrise-sunset__description sunrise-sunset__description_value_sunset"}).text









url = "https://yandex.ru/pogoda/moscow"
response = requests.get(url)
html = BeautifulSoup(response.content, "lxml")
#print(response.content)
print(gor(html))
print("-----------------------------")
print("температура:", temp(html))
print("На улице", opt(html))
#print("Восход", timesun(html)) Доделать

#Ctrl + shift + c. Выбор Элемента курсором
