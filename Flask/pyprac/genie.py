import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# code에서 client가 날린 것 처럼 하기 위한 설정
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.number

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.info > a.title.ellipsis

temp = soup.select('div.newest-list > div > table > tbody > tr')
for i in temp:
    rank = i.select_one('td.number').text[0:2].strip()
    title = i.select_one('td.info > a.title.ellipsis').text.lstrip()
    artist = i.select_one('td.info > a.artist.ellipsis').text
    print(rank, title, artist)