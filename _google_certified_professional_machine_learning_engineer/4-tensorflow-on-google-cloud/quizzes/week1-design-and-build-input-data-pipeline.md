# Quiz: Design and Build Input Data Pipeline

- [ ] **Question 1** What are distinct ways to create a dataset?

```
"데이터 세트를 만드는 고유한 방법은 무엇입니까?"
이해가 잘 안 가는 질문이다. 강의 비디오에서 이런 표현을 썼기 때문에 맞출 수 있었지만... 질문의 표현 자체가 별로 인 듯...
```

A data source constructs a Dataset from data stored in memory or in one or more files.

A data transformation constructs a dataset from one or more tf.data.Dataset objects. **[wrong guess]**


A data source constructs a Dataset from data stored in memory or in one or more files and a data transformation constructs a dataset from one or more tf.data.Dataset objects. **[correct answer]**

None of the options are correct.

**Question 2** Which is true regarding feature columns?

Feature columns describe how the model should use raw output data from your features dictionary.


Feature columns describe how the model should use raw output data from your TPU's.

Feature columns describe how the model should use `raw input data` from your features dictionary. **[correct answer]**


Feature columns describe how the model should use a graph to plot a line.

- [ ] **Question 3** Which of the following is true about embedding?

An embedding is a weighted sum of the feature crossed values. 

Embedding is a handy adapter that allows a network to incorporate spores or categorical data.

- spores n. 홀씨

The number of embeddings is the hyperparameter to your machine learning model. **[wrong guess]**

All options are correct. **[correct answer]**

**Question 4** What is the use of tf.keras.layers.TextVectorization?

It performs feature-wise normalization of input features.


It turns continuous numerical features into bucket data with discrete ranges.

It turns raw strings into an encoded representation that can be read by an Embedding layer or Dense layer. **[correct answer]**


It turns string categorical values into encoded representations that can be read by an Embedding layer or Dense layer.

- [ ] **Question 5** Which of the following is not a part of Categorical features preprocessing?

tf.keras.layers.CategoryEncoding

tf.keras.layers.Hashing **[Wrong guess]**


tf.keras.layers.IntegerLookup

tf.keras.layers.Discretization **[correct answer]**


Keras API Reference > ... > [Categorical features preprocessing layers](https://keras.io/api/layers/preprocessing_layers/categorical/)

- [CategoryEncoding layer](https://keras.io/api/layers/preprocessing_layers/categorical/category_encoding)
- [Hashing layer](https://keras.io/api/layers/preprocessing_layers/categorical/hashing)
- [StringLookup layer](https://keras.io/api/layers/preprocessing_layers/categorical/string_lookup)
- [IntegerLookup layer](https://keras.io/api/layers/preprocessing_layers/categorical/integer_lookup)

- [ ] **Question 6** Which of the following layers is non-trainable?

Discretization

Hashing **[correct answer]**


Normalization

StringLookup

Q6는 답 자체가 틀린 것일지도?
Keras > Developers guide > [Working with preprocessing layers](https://keras.io/guides/preprocessing_layers/)

* The adapt() method

```
Some preprocessing layers have an internal state that can be computed based on a sample of the training data. The list of stateful preprocessing layers is:

- `TextVectorization`: holds a mapping between string tokens and integer indices
- `StringLookup` and `IntegerLookup`: hold a mapping between input values and integer indices.
- `Normalization`: holds the mean and standard deviation of the features.
- `Discretization`: holds information about value bucket boundaries.

Crucially, these layers are **non-trainable**. Their state is not set during training; it must be set **before training**, either by initializing them from a precomputed constant, or by "adapting" them on data.

You set the state of a preprocessing layer by exposing it to training data, via the `adapt()` method
```

- [ ] **Question 7** When should you avoid using the Keras function adapt()?

When working with lookup layers with very large vocabularies **[correct answer]**


When using TextVectorization while training on a TPU pod


When using StringLookup while training on multiple machines via ParameterServerStrategy

When working with lookup layers with very small vocabularies

```
Why?
```

- [ ] **Question 8** Which of the following is a part of Keras preprocessing layers?

Image data augmentation


Image preprocessing 


Numerical features preprocessing 

All of the options are correct. **[correct answer]**