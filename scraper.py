import requests
from bs4 import BeautifulSoup

url = 'https://indianexpress.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

news_items = soup.find_all("li", attrs={'data-vr-contentbox': ''})

for item in news_items:
    h3_tag = item.find('h3')
    if h3_tag:
        a_tag = h3_tag.find('a')
        if a_tag:
            headline = a_tag.text.strip()
            link = a_tag['href'].strip()
            
            print(f'Headline: {headline}')
            print(f'Link: {link}')
            print('---')

