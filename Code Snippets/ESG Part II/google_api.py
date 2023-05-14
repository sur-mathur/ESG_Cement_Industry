!pip install GoogleNews
!pip install newspaper3k
from GoogleNews import GoogleNews
import pandas as pd
from newspaper import Article
import nltk
nltk.download('punkt')
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

googlenews=GoogleNews(start='05/01/2022',end='05/31/2023')
googlenews.search('cement, holcim, adbri')
result=googlenews.result()
df=pd.DataFrame(result)

list=[]
for i in df.index:
    dict={}
    article = Article(df['link'][i])
    article.download()
    article.parse()
    article.nlp()
    dict['Date']=df['date'][i]
    dict['Media']=df['media'][i]
    dict['Title']=article.title
    dict['Article']=article.text
    dict['Summary']=article.summary
    list.append(dict)

news_df=pd.DataFrame(list)
news_df.to_excel("news_articles.xlsx")
