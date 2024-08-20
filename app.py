

import requests

from bs4 import BeautifulSoup



URL_BASE = "https://edition.cnn.com"

URL = "https://edition.cnn.com/business"

HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

req = requests.get(URL, headers=HEADERS)

status = req.status_code
print(status)

if status == 200:
    
    soup = BeautifulSoup(req.content, "lxml")
    
    print(soup.title.text.strip())
    
    articles = []
    
    
    articles_c1 = soup.select("body > div.layout__content-wrapper.layout-no-rail__content-wrapper > section.layout__wrapper.layout-no-rail__wrapper > section.layout__main.layout-no-rail__main > div > section > div > div > div > div:nth-child(1) > div > div.zone__items.layout--wide-left-balanced-2 > div:nth-child(2) > div > div.stack__items > div > div.container_lead-plus-headlines__cards-wrapper > div > div > div > a")

    print(len(articles_c1))
    
    for article in articles_c1:
        
        href = URL_BASE + article["href"]
        
        articles.append(href)
        
        # print(href)

    
    articles_c2 = soup.select('body > div.layout__content-wrapper.layout-no-rail__content-wrapper > section.layout__wrapper.layout-no-rail__wrapper > section.layout__main.layout-no-rail__main > div > section > div > div > div > div:nth-child(1) > div > div.zone__items.layout--wide-left-balanced-2 > div:nth-child(1) > div > div.stack__items > div > div.container_lead-plus-headlines-with-images__cards-wrapper > div > div > div > a:nth-child(2)')
    
    print(len(articles_c2))
    
    for article in articles_c2:
        
        href = URL_BASE +  article['href']
        
        articles.append(href)
        
        # print(href)
        
    print(len(articles))