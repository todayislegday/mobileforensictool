import urllib.request
from urllib.request import urlopen
import re #정규표현식
from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import quote_plus
#여기까지가 크롤링에 필요한 것(위)



def image1(model): #크롤링코드
   
    baseUrl = 'https://www.google.com/search?q=' # 검색
    plusUrl = '&sxsrf=ALeKk03NvT-d6AcF-V5oJ8bgTDKo4J78Iw:1589354807929&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjxo_6FqLDpAhWx-GEKHdr6CUQQ_AUoAXoECBUQAw&biw=958&bih=927'
    url = baseUrl + quote_plus(model) + plusUrl #Url로 이동하기 위한 쿼리문자열 만들기

    print("url :",url)


    headers = {'User-Agent' : 'Mozilla/5.0'} #Mozilla요청, 안하면 403으로 크롤링 차단
    req = urllib.request.Request(url, headers=headers)

    html = urllib.request.urlopen(req) #url 열기

    soup = BeautifulSoup(html, 'lxml') #html.parser  ,,,, lxml

    IMG=[]
    result = []

    a= 1

    #img = soup.find_all('img')
    for img in soup.find_all("img"):
        IMG = (img['src'])

        if(a==3): #두번째 사진 사용
            break
        a += 1

    img_obj = {
        'title' : model,
        'image' : IMG
    }
    #print(img_obj)
    result.append(img_obj)

    return IMG #일단 이미지 주소만 반환



    



    












