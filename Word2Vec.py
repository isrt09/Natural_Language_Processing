# Word2Vec Model 

# !pip install gensim
import nltk
import urllib
import bs4 as bs
import re
from gensim.models import Word2Vec

# Gettings the data source
source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Global_warming').read()

# Parsing the data/ creating BeautifulSoup object
soup = bs.BeautifulSoup(source,'lxml')

# Fetching the data
text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text

# Preprocessing the data
text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\W',' ',text)
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)