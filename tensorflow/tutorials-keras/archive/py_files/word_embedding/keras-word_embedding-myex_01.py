#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:39:23 2019

@author: aimldl
"""

from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.embeddings import Embedding

docs = ['a bb',
		'ccc dddd',
		'eeeee f',
		'gg',
		'hhh iiii jjjjj k']

# integer encode the documents
token_list = []
for doc in docs:
    tokens = doc.split(' ')
    for token in tokens:
        token_list.append( token )
vocabulary = set( token_list )
print( vocabulary )
vocab_size = len( vocabulary )

from keras.preprocessing.text import one_hot
#encoded_docs = [one_hot(d, vocab_size) for d in docs]
encoded_docs = []
for doc in docs:
    encoded_doc = one_hot(doc, vocab_size)
    encoded_docs.append( encoded_doc )
print(encoded_docs)


x_train   = encoder.vectorize( train_data, num_words, method='one_hot_encoding' )