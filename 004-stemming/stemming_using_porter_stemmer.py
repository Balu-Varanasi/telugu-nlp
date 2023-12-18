# -*- encoding: utf-8 -*-

import nltk

from nltk.stem.porter import PorterStemmer


porter_stemmer = PorterStemmer()

# list of tokenized words
words = ["మహారాజులా", "పొందాలనుకున్నాడో", "మహారాజులు", "మహారాణిలు", "పొందాలనుకున్నారు", "ప్రతిపాదించారు"]

# stem's of each word
stem_words = []
for w in words:
    x = porter_stemmer.stem(w)
    stem_words.append(x)

# print stemming results
for e1, e2 in zip(words, stem_words):
    print(e1 + ' ----> ' + e2)