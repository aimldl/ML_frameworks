#!/usr/bin/env python
# coding: utf-8

# # Reuters Newswire Dataset
# * Draft: 2020-11-25 (Wed)
# 
# ## Description
# * Dataset for text classification tasks
# 

# ## Summary
# * 11,228 newswires from [Reuters](https://www.reuters.com/) (with Keras API)
#   * The classic Reuters-21578 dataset have been parsed and preprocessed
#   * each newswire is encoded as a list of word indexes (integers)
# * labeled over 46 topics; 46 classes
# 
# ## Common to text datasets
# * words are indexed by overall frequency in the dataset
#   * e.g. "3" encodes the 3rd most frequent word in the data
#   * "0" encodes any unknown word as a convention.
#   * This allows for quick filtering operations such as:
#     * only consider the top 10,000 most common words,
#     * but eliminate the top 20 most common words
# 
# ### Downloads
# * [Reuters-21578 Text Categorization Collection Data Set](https://archive.ics.uci.edu/ml/datasets/reuters-21578+text+categorization+collection), [Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php), [UCI](https://uci.edu/)
#   * [readme](https://kdd.ics.uci.edu/databases/reuters21578/README.txt)
#   * [reuters21578.tar.gz](https://kdd.ics.uci.edu/databases/reuters21578/reuters21578.tar.gz)
#     * 8.2MB; 28.0MB uncompressed
# * [Reuters-21578 benchmark corpus](https://www.kaggle.com/nltkdata/reuters), NLTK data, Kaggle
# * `reuters.load_data` function, Keras API reference
#   * See below for details.

# ## `reuters.load_data` function with Keras API
# Keras API reference > Built-in small datasets > [Reuters newswire classification dataset](https://keras.io/api/datasets/reuters/)
# * `load_data` function
# * `get_word_index` function
# 
# For details, see [Reuters newswire classification dataset](https://keras.io/api/datasets/reuters/).
# 
# ### `load_data` function
# loads the Reuters newswire classification dataset.
# 
# ```python
# tf.keras.datasets.reuters.load_data(
#     path="reuters.npz",
#     num_words=None,
#     skip_top=0,
#     maxlen=None,
#     test_split=0.2,
#     seed=113,
#     start_char=1,
#     oov_char=2,
#     index_from=3,
#     **kwargs
# )
# ```
# 
# returns
# * Tuple of Numpy arrays: (x_train, y_train), (x_test, y_test).
# * x_train, x_test: lists of sequences, which are lists of indexes (integers). If the num_words argument was specific, the maximum possible index value is num_words - 1. If the maxlen argument was specified, the largest possible sequence length is maxlen.
# * y_train, y_test: lists of integer labels (1 or 0).
# 
# #### Common to Keras's built-in small **text** datasets
# * start_char: int. The start of a sequence will be marked with this character. Defaults to 1 because 0 is usually the padding character.
# * oov_char: int. The out-of-vocabulary character. Words that were cut out because of the num_words or skip_top limits will be replaced with this character.
# * Note
#   * The 'out of vocabulary' character is only used for words that were present in the training set but are not included because they're not making the num_words cut here.
#   * Words that were not seen in the training set but are in the test set have simply been skipped.
#   
# ### `get_word_index` function
# ```python
# tf.keras.datasets.reuters.get_word_index(path="reuters_word_index.json")
# ```
# returns
# * the word index dictionary
#   * or a dict mapping words to their index in the Reuters dataset.
#   * Keys are word strings,
#   * values are their index.
# * path: where to cache the data (relative to ~/.keras/dataset).
