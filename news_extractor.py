import requests
from bs4 import BeautifulSoup
from newsplease import NewsPlease


def news_extractor(url):
    document = ''
    print('analysing url ' + url)
    count = 0
    try:
        r = requests.get(url)
        soup_content = BeautifulSoup(r.content, features='xml')
        items = soup_content.findAll('item')
        if r.status_code != 200:
            return

        for item in items:
            link = item.link.contents[0]
            count+=1
            article = NewsPlease.from_url(link)
            text = article.maintext.replace("\n", " ")
            text = text.replace("|", " ")
            title = article.title.replace("\n", " ")
            title = title.replace("|", " ")
            image = article.image_url.replace("\n", " ")
            temp = article.url + "|" + title + "|" + text + "|" + image
            document += temp + "\n"
    except Exception as exp:
        print('Extraction failed due to the below exception')
        print(exp)

    print('Number of links extracted ' + str(count))
    return document


print('Starting extracting')

file1 = open('news.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
file = open('detailed_analysis.csv', 'w')

for line in Lines:
    try:
        file.write(news_extractor(line.strip()))
        file.flush()
    except Exception as e:
        print('Scraping failed due to the below exception')
        print(e)
file.close()
