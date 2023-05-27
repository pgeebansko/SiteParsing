import requests
#  pip install beautifulsoup4;  pip install lxml
from bs4 import BeautifulSoup


def read_status(txt):
    p = txt.find('div', 'status')
    s = str(type(p))
    if s != "<class 'NoneType'>":
        if s == 'FT':
            return 'завършил'
        else:
            return 'играе се '+s
    else:
        return 'предстои - '+read_time(txt)


def read_time(txt):
    p = row.find('span', 'hour')
    s = str(type(p))
    result = ''
    if s != "<class 'NoneType'>":
        p = p.text
        lines = p.splitlines()
        s = lines[1].lstrip().rstrip()
        s = s.rpartition(', ')
        match_date = s[0]
        if len(match_date) != 0:
            match_date = 'на ' + match_date
        match_time = s[2]

        return f'ще се играе {match_date} в {match_time} ч.'
    else:
        return '----'


url = "https://gong.bg/livescore"
r = requests.get(url)
# print(r.text)
# soup = BeautifulSoup(r.text, 'html5lib')
soup = BeautifulSoup(r.text, 'lxml')
# print(soup)
tables = soup.findAll('div', class_='ls-schedule-table')
for table_html in tables:
    title = table_html.find('a', 'gtm-Livescore').find('h2').text
    match_rows = table_html.findAll('div', 'match-row')
    if len(match_rows)> 0 and ('Бундеслига, Германия' in title):
        print(title)
        for row in match_rows:
            host = row.find('div', 'host').text
            guest = row.find('div', 'guest').text
            print(f'      {host} - {guest}   ({read_status(row)}) ')

