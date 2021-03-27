import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Accept-Language":"ko-KR,ko" # 어떤 언어로 페이지를 받을지
    }

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))


# with open("movie.html","w",encoding="utf-8")as f:
#     # f.write(res.text)
#     f.write(soup.prettify()) # html문서를 예쁘게 출력
#     # 기존 페이지랑 다른 이유-> 헤더정보에 따라 다른 정보를 준다

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)