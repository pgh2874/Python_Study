import requests
res = requests.get("http://google.com")

# res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status() # 문제 발생시 오류출력후 프로그램 종료

# print("응답 코드 : ",res.status_code) #200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러 코드 ", res.status_code,"]")


# print("웹 스크래핑을 진행합니다.")

print(len(res.text))
print(res.text)

with open("mygoogle.html","w", encoding="utf8")as f:
    f.write(res.text)