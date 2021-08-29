import pandas as pd

df = pd.read_csv('data.csv')

x = df['test']

y= df['class']

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()

x = cv.fit_transform(x)

x.shape 

cv.vocabulary_

doc = x.toarray()

table = pd.DataFrame(doc, index= df, columns= cv.get_feature_names())

cv.get_feature_names()