import requests
from bs4 import BeautifulSoup

a = 1
b = 2
url = 'https://rp5.ru/Погода_в_Санкт-Петербурге'

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")


data = soup.find("span", class_="t_0").text
print(data)
