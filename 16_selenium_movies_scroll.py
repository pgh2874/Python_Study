
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()
url = "https://play.google.com/store/movies/top"
browser.get(url) # 페이지 이동


# 지정한 위치로 스크롤 내리기
# 모니터(해상도)의 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)") # 해상도 정보 : 1920 x 1080
# browser.execute_script("window.scrollTo(0, 2080)") # 해상도 정보 : 1920 x 1080

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)") # 맨 밑으로 스크롤 내리기


import time
interval = 2 # 2초에 한번 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    # 페이지 로딩 대기
    time.sleep(interval)
    
    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break
    
    prev_height = curr_height # 높이 값을 계속 갱신

print("스크롤 완료")

import requests
from bs4 import BeautifulSoup


soup = BeautifulSoup(browser.page_source,"lxml")

# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc","Vpfmgd"]}) # 클래스가 리스트안에 있는 것들과 일치하는 전부를 가져옴
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))


# with open("movie.html","w",encoding="utf-8")as f:
#     # f.write(res.text)
#     f.write(soup.prettify()) # html문서를 예쁘게 출력
#     # 기존 페이지랑 다른 이유-> 헤더정보에 따라 다른 정보를 준다

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    # print(title)

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "할인되지 않은 영화 제외")
        continue

    #할인된 가격
    price = movie.find("span",attrs={"class":"VfPpfd ZdBevf i5DZme"})
    if price:
        price = price.get_text()
    else:
        continue

    # 링크
    link = movie.find("a",attrs={"class":"JC71ub"})["href"]
    # 올바른 링크 https://play.google.com + link

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인된 가격 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 120)

    browser.quit()

