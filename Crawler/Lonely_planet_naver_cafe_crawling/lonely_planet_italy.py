from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests, re

# 총 페이지 개수를 센 후 article들의 url 리스트를 만드는 함수를 생성
def article_url(site) :
    html = requests.get(site, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    total_page = soup.select("#js-row--content > div.row__inner a.pagination__link.pagination__link--last")
    total_page = str(total_page[len(total_page)-1])
    total_page = int(re.search(">\d+",total_page).group()[1:])

    # range 마지막 숫자를 total +1로 바꿀것
    site_basic = site
    full_url = []
    for page in range(1,total_page+1) :
        site = site_basic + "?page=" + str(page)
        
        print(site)
        html = requests.get(site, headers=headers).text
        soup = BeautifulSoup(html, 'html.parser')
        result = soup.select("div > div.media__body > div > div.first-post.media__body > div.topic__title > a")
        
        pre_url = []
        for i in range(0,len(result)) :
            tem = str(result[i]).find(">")
            pre_url.append(str(result[i])[26:tem-1])

        for j in pre_url :
            tem = "https://www.lonelyplanet.com" + j + "?page="
            full_url.append(tem)
            
    return full_url

# article들을 하나의 문자열로 받아오는 함수를 생성
def article(urls) :
    review = []
    for url1 in urls :
        url_basic = url1 + str(1)
        html1 = requests.get(url_basic, headers=headers).text
        soup1 = BeautifulSoup(html1, 'html.parser')

        # 리뷰 페이지 수를 고려하여 url1을 생성
        page_nums = soup1.select("#js-row--content > div.row__inner a.pagination__link.pagination__link--last")
        try :
            page_nums = str(page_nums.pop())
            page_nums = page_nums[len(page_nums)-5:len(page_nums)-4]
        except :
            pass

        if page_nums == [] :
            result1 = soup1.select("#js-row--content > div.row__inner div.post__content > div.post__body.copy--forum.js-post-body > p ")
            result1 = "".join(str(result1))
            
            print(url_basic)
            
            result1 = re.sub('<a href.+blank">',"", result1)
            del_lists = ["<p>","</p>","<br>","<br/>", "</br>", "</a>"]
            for del_list in del_lists :
                result1 = result1.replace(del_list,"")

            review.append(result1)

        elif int(page_nums) >= 2 :
            result_list = []
            for page_num in range(0,int(page_nums)) :
                url2 = url1 + str(page_num+1)

                print(url2)

                html2 = requests.get(url2, headers=headers).text
                soup2 = BeautifulSoup(html2, 'html.parser')
                result1 = soup2.select("#js-row--content > div.row__inner div.post__content > div.post__body.copy--forum.js-post-body > p ")
                result1 = "".join(str(result1))
                
                result1 = re.sub('<a href.+blank">',"", result1)
                del_lists = ["<p>","</p>","<br>","<br/>", "</br>", "</a>"]
                for del_list in del_lists :
                    result1 = result1.replace(del_list,"")
                
                result_list.append(result1)
            
            result_list = " ".join(result_list)
            review.append(result_list)

        else :
            print("리뷰 페이지 관련 예외 발생 확인 바랍니다.")
    
    review = " ".join(review)
    print("done")
    return review

# user-agent 값을 추가함으로서 웹페이지에 AI가 아니라는 것을 전달
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
site ="https://www.lonelyplanet.com/thorntree/forums/europe-western-europe/italy"

urls = article_url(site)
reviews = article(urls)

with open("review_italy.txt","w", encoding="UTF-8") as f :
    f.write(reviews)

with open('./review_italy.txt', 'r', encoding="UTF-8") as r :
    reviews = r.read().lower()


len(reviews)

