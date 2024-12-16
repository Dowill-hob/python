
from bs4 import BeautifulSoup
import requests

# 실습1. 국립중앙박물관 관람 정보
html_mus = "https://www.museum.go.kr/site/main/home"
mus = requests.get(html_mus)
soup = BeautifulSoup(mus.text, 'html.parser')
time1 = soup.select_one("li.info > strong")

time2 = soup.select("div.info-txt > ul > li")

cost = soup.select_one("li.admission > strong")

print(f"{time1.text} {time2[0].text} {time2[1].text} {time2[2].text}")
print(f"{cost.text.strip()} / {time2[3].text}")

# 실습2. 전자 신문 메인 기사 크롤링

html_url = "https://www.etnews.com/20241203000250?mc=ns_001_00001"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, 'html.parser')
title = soup.select_one(".article_header #article_title_h2")

with open("news.txt", "w", encoding="utf-8") as file:
    file.write(f"{title.text.strip()}\n {date.text}")
    for i in contents:
        file.write(i.text)
        
# 웹스크래핑

# html_str = '''
# <html>
#     <body>
#         <div id="content">
#             <ul class="industry">
#                 <li> 인공지능 </li>
#                 <li> 빅데이터 </li>
#                 <li> 신재생에너지</li>
#             </ul>
#             <ul class ="comlang">
#                 <li> Python </li>
#                 <li> C++ </li>
#                 <li> Javascript </li>
#             </ul>
#         </div>
#     </body>
# </html>
# '''

# soup = BeautifulSoup(html_str, "html.parser")  # html 파싱
# first_ul = soup.find('ul')  # 처음으로 나오는 태그를 조회
# print(first_ul)
# print(first_ul.text)  # 태그없이 텍스트 출력

# all_ul = soup.find_all('li')  # 모든요소 li태그로 찾기
# print(all_ul)  # 리스트 형식
# print(all_ul[1].text)  # 리스트에서 text만 추출

# class_ul = soup.find('ul', attrs={'class': "comlang"})
# print(class_ul.text)

# 1개 요소 찾기 (id 선택자)
# first_select = soup.select_one("ul.industry")
# print(first_select)
# print(first_select.text)

# # 1개 요소 찾기
# all_select = soup.select_one('ul.comlang')
# print(all_select)
# print(all_select.text)

# # 모든요소 찾기
# all_select = soup.select('#content > ul')
# print(all_select)
# print(all_select[0].text)


# html_url = "https://www.seoul.go.kr/main/index.jsp"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, 'html.parser')
# all_nav = soup.select("nav > ul > li > a")
# # print(all_nav[0].text)
# for i in all_nav:
#     print(i.text)


# html_url = "https://news.kbs.co.kr/news/pc/view/view.do?ncd=8117340"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")
# title = soup.select_one(".headline-title")
# print("제목 : ", title.text.strip())
# contents = soup.select_one(".detail-body")
# print("내용 : ", contents.text.strip())

# with open("news.txt", "w", encoding="utf-8") as file:
#     file.write(contents.text.strip())


# # 명언 크롤링

# html_url = "https://quotes.toscrape.com/"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, 'html.parser')

# quote = soup.select(".quote > .text")
# contents = [i.text.strip() for i in quote]
# # print(f"{contents} \n")
# speak = soup.select(".author")
# author = [i.text.strip() for i in speak]
# # print(author)

# zipped = list(zip(contents, author))
# # print(zipped)

# for contents, author in zipped:
#     print(f"말한사람: {author} \n 내용: {contents}")
#     print()

# # 실습3환율정보 크롤링 하기
# html_url = "https://finance.naver.com/marketindex/"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, 'html.parser')

# USD = soup.select_one("a.usd >.point_dn > span.value")
# print("USD : ", USD.text.strip())
# JPY = soup.select_one("a.jpy >.point_dn > span.value")
# print("JPY(100엔) : ", JPY.text.strip())
# EUR = soup.select_one("a.eur >.point_dn > span.value")
# print("EUR : ", EUR.text.strip())
# CNY = soup.select_one("a.cny >.point_dn > span.value")
# print("CNY : ", CNY.text.strip())

# html_url = "https://finance.naver.com/item/main.naver?code=900270"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")
# title = soup.select_one(".h_company > .wrap_company >h2")
# print(f"주식 종목 : {title.text.strip()}")
# today_cost = soup.select_one(
#     ".content_wrap > #content > .spot > .rate_info > .today > .no_today > .no_up > .blind")
# print(f"오늘 현재가 : {today_cost.text.strip()} 원")
# icon = soup.select(
#     ".content_wrap > #content > .spot > .rate_info > .today > .no_exday > .no_up > .ico")
# yesterday_rate = soup.select_one(
#     ".content_wrap > #content > .spot > .rate_info > .today > .no_exday > .no_up > .blind")
# print(f"전일대비 : {icon[1].text.strip()}{yesterday_rate.text.strip()}")
