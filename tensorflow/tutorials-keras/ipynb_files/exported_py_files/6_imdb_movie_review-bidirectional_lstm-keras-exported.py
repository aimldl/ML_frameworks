#!/usr/bin/env python
# coding: utf-8

# # IMDB Movie Review Dataset Trained & Evaluated with Bidirectional LSTM (Keras)
# * Draft: 2020-11-25 (Wed)
# 
# ## Description
# * Binary classification problem in the field of Natural Language Processing (NLP)
# * Train a 2-layer bidirectional LSTM on the IMDB movie review sentiment classification dataset.
# 

# ## IMDB Movie Review Dataset
# ### Summary
# * 25,000 movie reviews from [IMDB](https://www.imdb.com/)
#   * Reviews have been preprocessed
#   * each review is encoded as a list of word indexes (integers)
#   * words are indexed by overall frequency in the dataset
#     * e.g. "3" encodes the 3rd most frequent word in the data
#     * "0" encodes any unknown word as a convention.
#     * This allows for quick filtering operations such as:
#       * only consider the top 10,000 most common words,
#       * but eliminate the top 20 most common words
# * labeled by sentiment (positive/negative); 2 classes
# * 50,000 training data; 10,000 test data
# 
# ### The Dataset
# [Large Movie Review Dataset](https://ai.stanford.edu/~amaas/data/sentiment/), [Andrew Maas](https://ai.stanford.edu/~amaas/), Stanford University
# * Publications using the dataset
#     * [Learning Word Vectors for Sentiment Analysis](https://ai.stanford.edu/~amaas/papers/wvSent_acl2011.pdf), Maas et.al, 2011.
# 
# ### Dataset with Keras API
# Keras API reference > Built-in small datasets > [IMDB movie review sentiment classification dataset](https://keras.io/api/datasets/imdb/)
# 
# ```python
# tf.keras.datasets.imdb.get_word_index(path="imdb_word_index.json")
# ```
# returns the word index dictionary. Keys are word strings, values are their index.
# * path: where to cache the data (relative to ~/.keras/dataset).
# 
# ```python
# tf.keras.datasets.imdb.load_data(
#     path="imdb.npz",
#     num_words=None,
#     skip_top=0,
#     maxlen=None,
#     seed=113,
#     start_char=1,
#     oov_char=2,
#     index_from=3,
#     **kwargs
# )
# ```
# loads the IMDB dataset.
# * start_char: int. The start of a sequence will be marked with this character. Defaults to 1 because 0 is used as \[unk\] or unknown.usually the padding character.
# * oov_char: int. The out-of-vocabulary character. Words that were cut out because of the num_words or skip_top limits will be replaced with this character.
# 
# For details, see [IMDB movie review sentiment classification dataset](https://keras.io/api/datasets/imdb/).
# 
# 

# ## Tutorials
# ### Official tutorial by Keras
# [Code examples](https://keras.io/examples) / [Natural language processing](https://keras.io/examples/nlp) / [Bidirectional LSTM on IMDB](https://keras.io/examples/nlp/bidirectional_lstm_imdb/)
# ``` text
# Author: fchollet
# Date created: 2020/05/03
# Last modified: 2020/05/03
# Description: Train a 2-layer bidirectional LSTM on the IMDB movie review sentiment classification dataset.
# ```
# 
# ### Unofficial tutorials
#  Google search: keras imdb example
#   * [IMDB - Sentiment analysis Keras and TensorFlow](https://www.kaggle.com/drscarlat/imdb-sentiment-analysis-keras-and-tensorflow), Kaggle

# ## Sample Source Code
# 

# In[2]:


import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

max_features = 20000  # Only consider the top 20k words

(x_train, y_train), (x_val, y_val) = keras.datasets.imdb.load_data(
    num_words=max_features
)
print( len(x_train), "training sequences" )
print( len(x_val), "validation sequences" )

maxlen = 200          # Only consider the first 200 words of each movie review
x_train = keras.preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)
x_val = keras.preprocessing.sequence.pad_sequences(x_val, maxlen=maxlen)


# In[2]:





# In[3]:


# Input for variable-length sequences of integers
inputs = keras.Input( shape=(None,), dtype="int32" )

# Embed each integer in a 128-dimensional vector
x = layers.Embedding( max_features, 128 )(inputs)

# Add 2 bidirectional LSTMs
x = layers.Bidirectional( layers.LSTM(64, return_sequences=True) )(x)
x = layers.Bidirectional( layers.LSTM(64) )(x)

# Add a classifier
outputs = layers.Dense( 1, activation="sigmoid" )(x)
model = keras.Model( inputs, outputs )
model.summary()


# In[4]:


model.compile( "adam", "binary_crossentropy", metrics=["accuracy"] )
model.fit( x_train, y_train, batch_size=32, epochs=5, validation_data=(x_val, y_val) )


# In[4]:




