import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)  # HTML을 받아온 것을 확인할 수 있다.

movies = soup.select('#old_content>table>tbody>tr')

for movie in movies:
    
    a_tag = movie.select_one('td.title>div>a')
    point = movie.select_one('td.point')
    if a_tag is not None:
        #a의 text를 찍어본다.
        rank = movie.select_one('td:nth-child(1)>img')["alt"]
        print(rank,a_tag,point)

#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img