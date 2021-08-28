import nltk
from nltk      import sent_tokenize
from nltk      import word_tokenize
from nltk.stem import WordNetLemmatizer

text = "I love Python Programming Language. I love to work with it. It is very easy to all for all ages peoples"

words      = nltk.word_tokenize(text)
lemmatizer = WordNetLemmatizer()

print(words)

print([lemma.lemmatize(word) for word in words])

lemmatization = [lemma.lemmatize(word) for word in words]
print(" ".join(lemmatization))
