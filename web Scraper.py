from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.scrapethissite.com/pages/').text
soup = BeautifulSoup(html_text, 'html.parser')

titles = soup.find_all('h3')

for title in titles:
    print(title.text)

