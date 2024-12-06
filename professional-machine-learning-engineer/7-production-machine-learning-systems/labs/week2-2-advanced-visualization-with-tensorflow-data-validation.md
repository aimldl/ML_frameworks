# Lab: Advanced visualizations with TensorFlow data validation

- 2 hours
- https://googlecoursera.qwiklabs.com/focuses/25711193?parent=lti_session

## Purpose

Understand how TensorFlow Data Validation (TFDV) can be used to 

- investigate
- visualize your dataset

Understand the dataset characteristics

- including
  - how it might change over time in your production pipeline

In our dataset

- looking at descriptive statistics
- inferring a schema
- checking for and fixing anomalies
- checking for drift and skew
  - compare your training, evaluation, and serving datasets
    - to make sure that they are consistent

## Objectives

- Install TFDV
- Compute and visualize statistics
- Infer a schema
- Check evaluation data for errors
- Check for evaluation anomalies and fix it
- Check for drift and skew
- Freeze the schema

## Steps to prepare the hands-on lab

1. Setup and requirements
2. Clone course repo within your Vertex AI notebooks instance
3. Open the notebook
4. Do the hands-on lab

## Hands-on lab 

Google docs > [Lab: Advanced Visualizations with TensorFlow Data Validation](https://docs.google.com/document/d/1MLvUG0Bdm0vqhRWeK2k_95dyX1b7ncNi5Bb5cEQ5UhE/edit#heading=h.eg0a9rka5ueb) 

Source code

```bash
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

[training-data-analyst](https://github.com/GoogleCloudPlatform/training-data-analyst)/[courses](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses)/[machine_learning](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning)/[deepdive2](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2)/

- [production_ml](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2/production_ml)/
  - [labs](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2/production_ml/labs) > [tfdv_advanced_taxi.ipynb](https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive2/production_ml/labs/tfdv_advanced_taxi.ipynb)
    - Each learning objective will correspond to a #TODO in the student lab notebook
  - [solutions](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2/production_ml/solutions) > [tfdv_advanced_taxi.ipynb](https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive2/production_ml/solutions/tfdv_advanced_taxi.ipynb)

My mirror files

- ipynb_files/
- - tfdv_advanced_taxi.ipynb
  - - Output all cleaned
  - [tfdv_advanced_taxi-working_solution.ipynb](ipynb_files/tfdv_advanced_taxi-working_solution.ipynb)

```
Caution:
At the beginning, don't forget to do the following when the packages are installed.

Restart the kernel (Kernel > Restart kernel > Restart).
Re-run the above cell and proceed further.
Note: Please ignore any incompatibility warnings and errors.
```



## Backgrounds

### [solutions/tfdv_advanced_taxi.ipynb](https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive2/production_ml/solutions/tfdv_advanced_taxi.ipynb)

- TFDV also provides functionalities to detect drift and skew.  TFDV  performs this check by comparing the statistics of the different  datasets based on the drift/skew comparators specified in the schema. 
- TFDV performs this check by comparing the statistics of the different  datasets based on the drift/skew comparators specified in the schema.

### Drift

Drift detection is supported for categorical features and between consecutive spans of data (i.e., between span N and span N+1), such as between  different days of training data.  We express drift in terms of [L-infinity distance](https://en.wikipedia.org/wiki/Chebyshev_distance), and you can set the threshold distance so that you receive warnings  when the drift is higher than is acceptable.  Setting the correct  distance is typically an iterative process requiring domain knowledge  and experimentation.

```markdown
[Chebyshev distance](https://en.wikipedia.org/wiki/Chebyshev_distance)
- Chebyshev distance (or Tchebychev distance), maximum metric, or L∞ metric[1]
- a metric defined on a vector space where the distance between two vectors is the greatest of their differences along any coordinate dimension.
- It is also known as chessboard distance, since in the game of chess the minimum number of moves needed by a king to go from one square on a chessboard to another equals the Chebyshev distance between the centers of the squares, if the squares have side length one, as represented in 2-D spatial coordinates with axes aligned to the edges of the board.[3] 
- For example, the Chebyshev distance between f6 and e2 equals 4.
```

### Skew

TFDV can detect three different kinds of skew in your data.

```
Schema  ?= feature columns
Feature ?= feature values
```

#### Schema Skew

- occurs when the  training and serving data do not conform to the same schema.

- Any expected deviations between the two should be  specified through environments field in the schema.
  - For example
    - The label feature is only present in the training data, not in serving

```
Both training and serving data are expected to adhere to the same schema.
```

#### Feature Skew

- occurs when 

  - the feature values that a model trains on are different from those seen at serving time. 

  - a data source that provides some feature values is modified between training and serving time

  - there is different logic for generating features between training  and serving. 
    - For example, if you apply some transformation only in one  of the two code paths.

#### Distribution Skew

- occurs when 
  - the distribution of the training dataset is significantly different from the distribution of the serving dataset. 

One of the key causes is 

- **using different code or** different **data sources** to generate the training dataset.
- **a faulty sampling mechanism** that chooses a non-representative subsample of the serving data to train on.
