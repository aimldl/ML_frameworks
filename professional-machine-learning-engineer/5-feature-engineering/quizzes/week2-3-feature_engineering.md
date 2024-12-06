# Quiz: Feature Engineering

**Grade: 62%**

Question 1
True or False: Feature Engineering is often one of the most valuable tasks a data scientist can do to improve model performance, for three main reasons:

1. You can isolate and highlight key information, which helps your algorithms "focus" on what’s important.

2. You can bring in your own domain expertise.

3. Once you understand the "vocabulary" of feature engineering, you can bring in other people’s domain expertise. 


- **True**
- 
  False


- [ ] Question 2
- [ ] What is one-hot encoding?

- **One-hot encoding is a process by which categorical variables are converted into a form that could be provided to neural networks to do a better job in prediction.**
- 
  One-hot encoding is a process by which numeric variables are converted into a form that could be provided to neural networks to do a better job in prediction.

- 
  One-hot encoding is a process by which numeric variables are converted into a categorical form that could be provided to neural networks to do a better job in prediction.

- One-hot encoding is a process by which only the hottest numeric variable is retained for use by the neural network. (wrong answer)

Question 3
What do you use the tf.feature_column.bucketized_column function for?

- To compute the hash buckets needed to one-hot encode categorical values

- 
  To count the number of unique buckets the input values falls into

- **To discretize floating point values into a smaller number of categorical bins**
- 
  None of the options are correct.


Question 4
What is a feature cross? 

- A feature cross is a synthetic feature formed by adding (crossing) two or more features. Crossing combinations of features can provide predictive abilities beyond what those features can provide individually.

- **A feature cross is a synthetic feature formed by multiplying (crossing) two or more features. Crossing combinations of features can provide predictive abilities beyond what those features can provide individually.** (correct guess)
- 
  A feature cross is a synthetic feature formed by dividing (crossing) two or more features. Crossing combinations of features can provide predictive abilities beyond what those features can provide individually.

- 
  None of the options are correct.


Question 5
Which of the following statements are true regarding the ML.EVALUATE function?

- The ML.EVALUATE function can be used with linear regression, logistic regression, k-means, matrix factorization, and ARIMA-based time series models.

- 
  The ML.EVALUATE function evaluates the predicted values against the actual data.

- 
  You can use the ML.EVALUATE function to evaluate model metrics.

- **All of the options are correct.**

Question 6
What is the significance of ML.FEATURE_CROSS?

 ```
 (아래 문장이) 뭔소리인지 하나도 모르겠다.
 ```

- **ML.FEATURE_CROSS generates a STRUCT feature with all combinations of crossed categorical features except for 1-degree items.** (correct guess)
- 
  ML.FEATURE_CROSS generates a STRUCT feature with few combinations of crossed categorical features except for 1-degree items.

- ML.FEATURE_CROSS generates a STRUCT feature with all combinations of crossed categorical features including 1-degree items. (wrong guess)
- 
  None of the options are correct.


Question 7
Which of the following statements are true regarding the ML.BUCKETIZE function?

 ```
 Not sure of array_split_points
 ```

- ML.BUCKETIZE is a pre-processing function that creates buckets by returning a STRING as the bucket name after numerical_expression is split into buckets by array_split_points. 

- 
  It bucketizes a continuous numerical feature into a string feature with bucket names as the value.

- **Both options are correct.**
- 
  None of the options are correct.


Question 8
Which of the following is true about Feature Cross?

```
I don't quite understand "...learn separate weights for each combination of features."
```

- It is a process of combining features into a single feature. (wrong guess)
- 
  Feature Cross enables a model to learn separate weights for each combination of features.

- **Both options are correct.**
- 
  None of the options are correct.
