import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
nltk.download("popular")

paragraph = "I love Python Programming Languages. It is easy to all. I love to work with it"

sentence = nltk.sent_tokenize(paragraph)
words    = nltk.word_tokenize(paragraph)

print(type(sentence))
print(type(word))

print(len(sentence))
print(len(word))

vocabulary = []
for word in words:
	vocabulary.append(word)

print(vocabulary)

