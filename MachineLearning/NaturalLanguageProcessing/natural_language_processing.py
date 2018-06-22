# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords') # Downloading list of neutral words (the, this, that, etc)
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

# Importing the dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3) # DELIMITER = TAB, IGNORE DOUBLE QUOTES


# Create a Corpus of 1000 reviews (a collection of texts)
corpus = []

# Create for looping all reviews
for i in range(0, 1000):
    # Cleaning the dataset
    clean_review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i]) # Removed everythin except a-z, A-Z and added spaces
    clean_review = clean_review.lower() # Lower case
    clean_review = clean_review.split()
    
    # Steming - loving&loved&love = love)
    ps = PorterStemmer()
    
    # Steming for portuguese
    # nltk.download('rslp')
    #PT_stem = nltk.stem.RSLPStemmer() # Deixa somente a raiz da palavra
    
    # For loop, check if word is relevant with stopwords, and remove it
    clean_review = [ps.stem(word) for word in clean_review if not word in set (stopwords.words('english'))]
    
    # Joining all words of each review in a string instead of list
    clean_review = ' '.join(clean_review)
    
    # Add clean_review to corpus
    corpus.append(clean_review)

# Create the Bag of Words model - a sparse matrix of 1000 rows (each review) and N columns (each word), cells filled by the number of times that word appears in that review
count_vectorizer = CountVectorizer(max_features = 1500) # max_features is filtering less frequent words
sparse_matrix = count_vectorizer.fit_transform(corpus).toarray()

# Getting the real results from the dataset (liked = 1, not liked = 0)
y = dataset.iloc[:, 1].values

# Finaly, using classification models (most common: naive bayes, decision tree, random forest)
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB

# BUILD TRAINING (75%) AND TEST SETS (25%) - random_state to spit same results
x_train, x_test, y_train, y_test = train_test_split(sparse_matrix, y, test_size = 0.2, random_state = 0)
 
# FIT CLASSIFIER TO MODEL
classifier = GaussianNB()
classifier.fit(x_train, y_train)

# PREDICT A NEW RESULT
y_pred = classifier.predict(x_test)

# MAKING CONFUSION MATRIX 
cm = confusion_matrix(y_test, y_pred)








