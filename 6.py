import requests, pandas as pd
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/product-reviews/ITEM_ID?page=1"  # replace ITEM_ID

r = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(r.text, 'lxml')

names = [i.text for i in soup.select('p._2sc7ZR._2V5EHH')]
ratings = [i.text for i in soup.select('div._3LWZlK._1BLPMq')]
titles = [i.text for i in soup.select('p._2-N8zT')]
reviews = [i.text for i in soup.select('div.t-ZTKy div')]
dates = [i.text.split('Certified Buyer')[0].strip() for i in soup.select('p._2sc7ZR+div')]

df = pd.DataFrame({'Name':names, 'Rating':ratings, 'Tag':titles, 'Review':reviews, 'Date':dates})
print(df.head())
