from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time, os, sys, requests, re

def selenium_start(id, pw, url) :
    driver.get('https://nid.naver.com/nidlogin.login')

    driver.execute_script("document.getElementsByName('id')[0].value=\'"+ id +"\'")
    driver.execute_script("document.getElementsByName('pw')[0].value=\'"+ pw +"\'")                     
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

    time.sleep(2)
    driver.get(url)


id = 'swim1123'
pw = 'sg2936!'


# driver = webdriver.Chrome('./chromedriver/chromedriver.exe')
# selenium_start(id,pw,"https://cafe.naver.com/firenze.cafe")
# soup = bs(driver.page_source, 'html.parser')

# # 국가별 게시판 명과 주소 가져오기
# country_name = soup.select("#group155 > li>a")[0].text
# country_url = soup.select("#group155 > li>a")[0]['href']

# driver.get("https://cafe.naver.com/firenze.cafe"+country_url)

# # 이탈리아 게시판에서 링크 추출
# driver.switch_to.frame('cafe_main')

# nums =list(range(1,30,2))
# article_url = []

# for j in range(1,1001) :
#     driver.get("https://cafe.naver.com/ArticleList.nhn?search.clubid=10209062&search.menuid=23&search.boardtype=L&search.totalCount=151&search.page="+str(j))
#     driver.switch_to.frame('cafe_main')
#     for i in nums :
#         selector = "#main-area tr:nth-child("+str(i)+") > td.board-list > span > span > a"
#         review_urls = driver.find_element_by_css_selector(selector).get_attribute("href")
#         article_url.append(review_urls)

# # url 목록 저장
# with open("article_url_kor.txt","w", encoding="UTF-8") as f :
#     f.write(str(article_url))

# 저장된 url 불러오고 전처리
with open('./article_url_kor.txt', 'r', encoding="UTF-8") as r :
    article_url_kor = r.read()
article_url_kor = article_url_kor.replace("[","")
article_url_kor = article_url_kor.replace("]","")
article_url_kor = article_url_kor.replace("'","")
article_url_kor = article_url_kor.split(", ")

# 불러온 링크로 스크래핑
driver = webdriver.Chrome('./chromedriver/chromedriver.exe')
selenium_start(id,pw,article_url_kor[0])

# for test
driver.get(article_url_kor[1499])

driver.switch_to.frame('cafe_main')
title = driver.find_element_by_css_selector("div > div.tit-box > div.fl > table > tbody > tr > td > span").text
content = driver.find_element_by_css_selector("#tbody").text

comment_num = int(driver.find_element_by_css_selector("#comment").text[3:])
comments = []
for i in range(1,comment_num*2,2) :
    comment_sel = "#cmt_list > li:nth-child(" + str(i) +") > div > p > span"
    if driver.find_element_by_css_selector("#cmt_list > li:nth-child("+str(i)+ ") > div > p > span").get_attribute('class') == "comm_body" :
        comment = driver.find_element_by_css_selector("#cmt_list > li:nth-child("+str(i)+ ") > div > p > span").text
        comments.append(comment)

len(comments)

#post_1571551 > div > div.tit-box > div.fl > table > tbody > tr > td:nth-child(1) > span

#101 안됨
#post_6934443 > div > div.tit-box > div.fl > table > tbody > tr > td:nth-child(2) > span
#post_6934006 > div > div.tit-box > div.fl > table > tbody > tr > td:nth-child(1) > span
#post_6933962 > div > div.tit-box > div.fl > table > tbody > tr > td:nth-child(1) > span
#post_6933856 > div > div.tit-box > div.fl > table > tbody > tr > td:nth-child(2) > span
#post_6933850 > div > div.tit-box > div.fl > table > tbody > tr > td:nth-child(1) > span
#post_6933390 > div > div.tit-box > div.fl > table > tbody > tr > td:nth-child(1) > span
#post_6932988 > div > div.tit-box > div.fl > table > tbody > tr > td:nth-child(2) > span