from bs4 import BeautifulSoup
import requests, re, string

site = "https://en.wikipedia.org/wiki/List_of_cities_in_Italy"
html = requests.get(site).text

soup = BeautifulSoup(html, 'html.parser')
city_names = soup.select("#mw-content-text > div > table > tbody > tr > td:nth-of-type(2) > a[title]")
city_names = list(city_name)

city_list_eng = []
for city_name in city_names :
    city_name = str(city_name)
    city_name = re.sub('<a .+">',"", city_name)
    city_name = city_name.replace("</a>","")
    city_list_eng.append(city_name)

city_list_eng

with open("city_list_eng.txt","w", encoding="utf-8") as f :
    f.write(str(city_list_eng))

# 영어 목록을 구글맵에 검색하여 영문 명과 한글 명은 구글맵과 일치 시킴




# 론리플래닛 데이터에서 각 도시가 언급되는 수를 확인
frequency = {}
document_text = open('./review_italy.txt', 'r', encoding="UTF-8")
text_string = document_text.read().lower()
document_text.close()

city_refer = {}
for city_eng in city_list_eng :
    city_eng = city_eng.lower()
    match_pattern = re.findall(city_eng+".", text_string)
    refer = len(match_pattern)
    city_refer[city_eng] = refer

city_refer