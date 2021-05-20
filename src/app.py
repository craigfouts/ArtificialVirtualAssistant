'''
Created by: Craig Fouts
Created on: 5/20/2021
'''

import json
import nltk
import numpy as np
import random
import string
import tensorflow as tf
from nltk.stem import WordNetLemmatizer
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

words = []
classes = []
doc_X = []
doc_Y = []

with open('data/intents.json') as file:
    data = json.load(file)

for intent in data['intents']:
    for pattern in intent['patterns']:
        tokens = nltk.word_tokenize(pattern)
        words.extend(tokens)
        doc_X.append(pattern)
        doc_Y.append(intent['tag'])
    classes.append(intent['tag']) if intent['tag'] not in classes else None

words = [lemmatizer.lemmatize(word.lower())
         for word in words if word not in string.punctuation]

words = sorted(set(words))
classes = sorted(set(classes))

training = []
out_empty = [0] * len(classes)
