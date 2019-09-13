import sys
import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.metrics import *

# create dictionnary of words from article
def countWordInstance(article):
	if len(sys.argv) == 4:
		print("function 'countWordInstance' called")
	dicoArticle = {}
	for word in article:
		if word in dicoArticle:
			dicoArticle[word] += 1
		else:
			dicoArticle[word] = 1
	return dicoArticle

# show a graphic with each word followed by iteration
def showZipfSLow(art):
	if len(sys.argv) == 4:
		print("function 'showZipfSLow' called")
	# conversion into lowercase and uppercase and
	# replace text with another text and tokenization of sentences into words
	lemmatizer_output = WordNetLemmatizer()
	tmpArticle = lemmatizer_output.lemmatize(art)
	article = nltk.word_tokenize(tmpArticle.lower())

	#plt.title(article[0])
	
	#article.pop(0) # remove the name of article
	dicoArticle = countWordInstance(article)
	items = sorted(dicoArticle.items(), key = lambda x : x[1], reverse=True)
	keys, values = [], []
	for key, value in items:
		keys.append(key)
		values.append(value)

	plt.bar(range(len(dicoArticle)), values, align='center')
	plt.xticks(range(len(dicoArticle)), keys)
	plt.show()

#showZipfSLow(article2)


# find the two nearest sentences in the article on the same topic
def findTwoNearest(a1, a2):
	if len(sys.argv) == 4:
		print("function 'findTwoNearest' called")
	"""
	steps:
	1. upper to lower
	2. lemmatization
	3. tokenization by sentence then by words
	4. remove stopwords
	5. similarity measure : Jaccard's coefficient || edit_distance
	"""
	# 1. upper to lower
	a1p, a2p = a1.lower(), a2.lower()
	if len(sys.argv) == 4:
		print("step 1 'upper to lower' [Done]")

	# 2. lemmatization
	lemmatizer_output = WordNetLemmatizer()
	a1p = lemmatizer_output.lemmatize(a1p)
	a2p = lemmatizer_output.lemmatize(a2p)
	if len(sys.argv) == 4:
		print("step 2 'lemmatization' [Done]")

	# 3.1 tokenization by sentence
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	a1_sentences = tokenizer.tokenize(a1p)
	a2_sentences = tokenizer.tokenize(a2p)

	# 3.2 tokenization by words from previous tokenization
	a1_array, a2_array = [], []
	for sentence in a1_sentences:
		tokenizer=RegexpTokenizer("[\w]+")
		a1_array.append(tokenizer.tokenize(sentence))

	for sentence in a2_sentences:
		tokenizer=RegexpTokenizer("[\w]+")
		a2_array.append(tokenizer.tokenize(sentence))

	if len(sys.argv) == 4:
		print("step 3 'tokenization' [Done]")

	# 4. remove stopwords
	stops = set(stopwords.words('english'))
	for i in range(len(a1_array)):
		a1_array[i] = [word for word in a1_array[i] if word not in stops]
	for i in range(len(a2_array)):
		a2_array[i] = [word for word in a2_array[i] if word not in stops]
	
	if len(sys.argv) == 4:
		print("step 4 'stopwords removed' [Done]")

	min_value = 1.0
	index, jindex = 0, 0
	for i in range(len(a1_array)):
		X = set(a1_array[i])
		for j in range(len(a2_array)):
			Y = set(a2_array[j])
			j_distance = jaccard_distance(X,Y)
			if j_distance < min_value:
				min_value = j_distance
				index, jindex = i, j

	if len(sys.argv) == 4:
		print("step 5 'Jaccard distance computed' [Done]")
	print("Min Jaccard distance: ",min_value, "\n From article 1: ", index, "\n From article 2: ",jindex)
	print(a1_sentences[index])
	print(a2_sentences[jindex])

# sys checking
if len(sys.argv) >= 3:
	# open and read articles
	article1 = open(sys.argv[1], "r").read()
	article2 = open(sys.argv[2], "r").read()
	findTwoNearest(article1,article2)
else:
	print("Error with your previous command.\n Try something like: \n\n $ python3 wp1.py your_article1.txt your_article2.txt \n\n")
	print("For activing debuging mode, add '-' add the end like \n\n  $ python3 wp1.py your_article1.txt your_article2.txt -")