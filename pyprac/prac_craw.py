import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://root:1860@cluster0.8fpka1h.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# code에서 client가 날린 것 처럼 하기 위한 설정
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)
# 끝단의 headers 부분이 client가 날린 것 처럼 하기 위해 넣어준 설정
soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
# 웹 페이지 '검사'의 코드 부분에서 copy selecter 한 것이다
# print(title)
# print(title.text) # 해당 test가 보임
# print(title['href']) # 태그 안의 값만 보이게 하는 것

#old_content > table > tbody > tr:nth-child(3) > td.title > div > a
#old_content > table > tbody > tr:nth-child(4) > td.title > div > a

movies = soup.select('#old_content > table > tbody > tr')

for i in movies:
    a = i.select_one('td.title > div > a')
    if a is not None:
        title = a.text
        rank = i.select_one('td:nth-child(1) > img')['alt']
        star = i.select_one('td.point').text
        doc = {
            'title':title,
            'rank':rank,
            'star':star
        }
        db.movies.insert_one(doc)