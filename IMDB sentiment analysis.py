# Importing the libraries
import numpy as np
import re
import pickle 
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


# Importing the dataset
from sklearn.datasets import load_files
reviews_train = load_files('train/')
reviews_test = load_files('test/')
X_train,y_train = reviews_train.data,reviews_train.target
X_test,y_test = reviews_test.data,reviews_test.target
X = X_train + X_test
y = np.concatenate([y_train,y_test])
X = X[:50000]
y = y[:50000]


# Unpickling dataset
X_in = open('X.pickle','rb')
y_in = open('y.pickle','rb')
X = pickle.load(X_in)
y = pickle.load(y_in)


# Improving the stop words list
stop_words = stopwords.words('english')
uncheck_words = ['don','won','doesn','couldn','isn','wasn','wouldn','can','ain','shouldn','not']

# Creating the corpus which is the input to TFIDFVectorizer
corpus = []
for i in range(0, len(X)):
    antonyms = []
    review = re.sub(r'\W', ' ', str(X[i]))
    review = re.sub(r'\d', ' ', review)
    review = review.lower()
    review = re.sub(r'br[\s$]', ' ', review)
    review = re.sub(r'\s+[a-z][\s$]', ' ',review)
    review = re.sub(r'b\s+', '', review)
    review = re.sub(r'\s+', ' ', review)
    word_list = review.split(' ')
    newword_list = []
    temp_word = ''
    for word in word_list:
        if temp_word in uncheck_words:
            if word not in stop_words:
                word = 'not_' + word
                temp_word = ''
        if word in uncheck_words:
            temp_word = word
        if word not in uncheck_words:
            newword_list.append(word)
    review = ' '.join(newword_list)
    corpus.append(review)    
