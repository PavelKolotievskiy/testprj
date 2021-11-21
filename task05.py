#Работа с HTML Скачать содержимое страницы https://epam.com с помощью requests Посчитать количество тегов div на этой странице (лучше использовать для этого библиотеку beautifulsoup4)
from bs4 import BeautifulSoup, ResultSet
import requests

r = requests.get('https://epam.com')
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')
div_html: ResultSet = soup.find_all('div')
print(len(div_html))


#Работа с sqlite. С помощью SQL запросов создать таблицу содержаюую 2 стобца: номер и имя Добавить три строки с данными. Получить данные из таблицы и распечатать их на экране.
import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''create table contacts (id int, name varchar(255))''')
c.execute("insert into contacts (id, name) select 1, 'Ivan Ivanov'")
c.execute("insert into contacts (id, name) select 2, 'Petr Petrov'")
c.execute("insert into contacts (id, name) select 3, 'Sergey Sergeev'")
for row in c.execute("select id, name from contacts"):
    print(row)


