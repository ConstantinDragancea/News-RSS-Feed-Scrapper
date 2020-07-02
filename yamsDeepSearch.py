from bs4 import BeautifulSoup
import requests as req

page_link = 'https://news.yam.md/'

def search_article(article_link, *keywords):
    yams_summary = req.get(page_link + article_link).content
    yams_soup = BeautifulSoup(yams_summary, 'html.parser')
    news_anchor = yams_soup.findAll('p')
    news_anchor = news_anchor[1].findAll('a')
    article_link = news_anchor[0]['href']
    # print('attempting link {}'.format(article_link))
    article = req.get(article_link).content
    a_soup = BeautifulSoup(article, 'html.parser')
    paragraphs = a_soup.findAll('p')
    paragraphs = [p.text.lower() for p in paragraphs]
    flag = False
    for word in keywords:
        for paragraph in paragraphs:
            if word in paragraph:
                print(article_link)
                return

def getLinks(*keywords):
    page = req.get(page_link).content
    soup = BeautifulSoup(page, 'html.parser')
    links = soup.findAll('a')
    links = [link for link in links if link.has_attr('href') and 'story' in link['href']]
    for link in links:
        search_article(link['href'], *keywords)
