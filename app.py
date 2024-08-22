
# Headline
# Cover
# Related_Content
# Illustrations_Url
# Full_Article
# Publication_Date
# Article_URL
# Posted_by 



import pandas as pd

import requests

from bs4 import BeautifulSoup



URL_BASE = "https://edition.cnn.com"

URL = "https://edition.cnn.com/business"

HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
def get_articles_link():
    articles = []
    
    req = requests.get(URL, headers=HEADERS)
    
    status = req.status_code
    # print(status)

    if status == 200:
        
        soup = BeautifulSoup(req.content, "lxml")
        
        # print(soup.title.text.strip())
        
        
        
        
        articles_c1 = soup.select("body > div.layout__content-wrapper.layout-no-rail__content-wrapper > section.layout__wrapper.layout-no-rail__wrapper > section.layout__main.layout-no-rail__main > div > section > div > div > div > div:nth-child(1) > div > div.zone__items.layout--wide-left-balanced-2 > div:nth-child(2) > div > div.stack__items > div > div.container_lead-plus-headlines__cards-wrapper > div > div > div > a")

        # print(len(articles_c1))
        
        for article in articles_c1:
            
            href = URL_BASE + article["href"]
            
            articles.append(href)
            
            # print(href)

        
        articles_c2 = soup.select('body > div.layout__content-wrapper.layout-no-rail__content-wrapper > section.layout__wrapper.layout-no-rail__wrapper > section.layout__main.layout-no-rail__main > div > section > div > div > div > div:nth-child(1) > div > div.zone__items.layout--wide-left-balanced-2 > div:nth-child(1) > div > div.stack__items > div > div.container_lead-plus-headlines-with-images__cards-wrapper > div > div > div > a:nth-child(2)')
        
        # print(len(articles_c2))
        
        for article in articles_c2:
            
            href = URL_BASE +  article['href']
            
            articles.append(href)
            
            # print(href)
            
        print(f'The number of articles found at {URL} is {len(articles)}')
        
    else:
        print("No article found")
        articles = []
        
        
    return articles


def extract_articles_content():
    
    articles = get_articles_link()
    
    
    data = []
    
    for article in articles:
        Article_URL = article
        req = requests.get(article, headers=HEADERS)
        
        status = req.status_code
        # print(status)

        if status == 200:
            
            soup = BeautifulSoup(req.content, "lxml")
            Headline = soup.select_one(".headline__text").text.strip()
            container = soup.select_one("div.article__content-container")
            
            paragraphs = container.select('p.paragraph.inline-placeholder.vossi-paragraph-primary-core-light')
            
            Illustrations_Url = [item.find("a").get("href") for item in paragraphs if item.find("a") is not None]
            
            Full_Article = [item.text.strip() for item in paragraphs]
            
            Publication_Date = soup.select_one("div.timestamp.vossi-timestamp-primary-core-light").text.strip()
            
            
            authors = soup.select_one("div.byline__names").select("a")
            Posted_by = [[item.text.strip(), item.get("href")] for item in authors]
            
            if len(soup.select("a.related-content__link"))>0:
                Related_Content = [item.get('href') for item in soup.select("a.related-content__link")]
            else:
                Related_Content = []
                
            Cover = None
            
            row = [Headline, Article_URL, Full_Article, Illustrations_Url, Publication_Date, Related_Content, Cover, Posted_by]
    
            data.append(row)
            
    return data

        
    
def CNN_Data_scraper():
    
    
    HEADERS = ["Headline", "Article URL", "Full Article", "Illustrations Url", "Publication Date", "Related Content", "Cover", "Posted by"]

    data = extract_articles_content()
    
    
    df = pd.DataFrame(data, columns= HEADERS)
    
    df.to_csv("Lastest_Business_Article_From_CNN.csv")
    
    
    
