! pip install beautifulsoup4
! pip install requests
! pip install urllib

from bs4 import BeautifulSoup
import urllib.request,sys,time
import requests
from newspaper import Article
from newspaper import Config

import nltk
#config will allow us to access the specified url for which we are #not authorized. Sometimes we may get 403 client error while parsing #the link to download the article.
nltk.download('punkt')

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent
search='adbri'
url='https://www.globalcement.com/news/itemlist/search?searchword='
page = requests.get(url)
page.status_code
soup = BeautifulSoup(page.text, "html.parser")

for j in links:
    Link = j.find_all("h3",attrs={'class':'genericItemTitle'})
    list=[]
    for i in Link:
        dict={}
        article = Article("https://www.globalcement.com"+i.find('a')['href'].strip(),config=config)
        article.download()
        article.parse()
        article.nlp()
        dict['Date']=i.find('span').text.strip()
        dict['Title']=i.find('a').text.strip()
        dict['Article']=article.text
        dict['Summary']=article.summary
        list.append(dict)

news_df=pd.DataFrame(list)
news_df