# Week2-4-Training, Tuning and Serving on AI Platform

# Memo

- SKlearn with hyperparameter tuning is used to train the model in this example

- The system overview is explained one component after another
  - in sub-sequent videos
  - together with 
    - the gcloud command
    - Python code (with SKlearn)
    - Dockerfile
    - config.yaml

## Overview

ML model building process



Building and operationalizing the model



- train.py
- Dockerfile
- config.yaml

MLOps building blocks on Google Cloud in this module



System overview



Where we are going next



## Training, Tuning and Serving your model on AI Platform

### Create a reproducible dataset

System overview



UCI Machine Learning Repository > Covertype dataset



Split the dataset and experiment with models



Getting a random 80% of your dataset for training is easy



- RAND() < 0.8
- Instead use the last few hash digits.

However experimentation requires repeatability

- You need to know which specific data was involved in training, validation, and testing.

Native random splitting is not repeatable



- RAND() will return different results each time.

Solution: Use hasing and modulo operators to split a dataset into training/validation





- FARM_FINGERPRINT
  - WHERE MOD(ABS(FARM_FINGERPRINT(date)), 10) < 8



- Hash value on the date will always return the same value.
- Then we use a modulo operator to pull only 80% of that data based on the last few hash digits.
- WHERE MOD(ABS(FARM_FINGERPRINT(date)), 10) == 9



Which field to hash on?





- TO_JSON_STRING(cover)

Create a training split



Do the same for the validation split

 

### Implement a tunable model

System overview



ML models are functions with parameters and hyperparameters



ML model: Sklearn pipeline



- ColumTransformer
- Pipeline > SGDClassifier (Stochastic Gradient Descent)
- set_params (hyperparameters)
- fit
- score

How to use AI Platform for hyperparameter tuning



- cloudml-hypertune

- Use config.yaml that contains hyperparameters

1. Make the hyperparameter a command-line argument



- import fire
  - fire generates the command-line argument
- Python train.py ...

2. Set up cloudml-hypertune to record training metrics



- import hypertune
  - imports cloudml-hypertune

3. Export the final trained model



- import pickle
  - pickle.dump( ... )

4. Supply hyperparameters to the training job



- config.yaml
  - trainingInput:
    - hyperparameters:



- gcloud ai-platform jobs submit training ...

### Build and push a training container

System overview



Create the training Docker container



```dockerfile
# Dockerfile
FROM gcr.io/deeplearning-platform-release/base-cpu
RUN pip install -U fire coludml-hypertune scikit-learn==0.20.4 pandas=0.24.2
WORKDIR /app
COPY train.py .
ENTRYPOINT ["python", "train.py"]
```



```bash
gcloud builds submit --tag gcr.io/$PROJECT/$IMAGE:$TAG $TRAINING_APP_FOLDER
```

### Train and tune a model

System overview



Start the hyperparameter tuning job on AI Platform



- gcloud ai-platform jobs submit training ...



- AI Platform > Jobs



- AI Platform > Jobs > Jobs Details



Query AI Platform Training for the best hyperparameters



```python
from googleapiclient import discovery

ml = discovery.build('ml', 'v1')

job_id = 'projects/{}/jobs/{}'.format(PROJECT_ID, JOB_NAME)
request = ml.projects().jobs().get(name=job_id)

response = request.execute()

alpha = response['trainingOutput'] ...
max_iter = response['trainingOutput'] ...
```

Retrain with the best hyperparameters and export



```bash
gcloud ai-platform jobs submit training $JOB_NAME \
  --region=$REGION
  --job-dir=$JOB_DIR \
  ...
  # The same command without config.yaml
  -- \
  # Instead use the best hyperparams!
  --alpha=$alpha
  --max_iter=$max_iter \
  --nohptune
```

Model now exported as model.pkl on Cloud Storage



```python
if not hptune:
    	model_filename = 'model.pkl'
        with open(model_filename, 'wb') as model_file:
            pickle.dump(pipeline, model_file)
        gcs_model_path = "{}/{}".format(job_dir, model_filename)
        subprocess.check_call(['gsutil', 'cp', model_filename, gcs_model_path], stderr=sys.stdout)
```

### Serve and query a model

System overview



- REST API call

AI Platform Prediction makes deploying models easy



- model.pkl
- REST API call

Create a model resource



- gcloud ai-platform models ...
- First create the model object

```bash
gcloud ai-platform models create $model_name \
  --region=$REGION
  --labels=$labels \
```

Create a model version



```bash
gcloud ai-platform models create {model_version} \
  --mode=$model_name \
  # where model.pkl is exported
  --origin=$JOB_DIR \
  --runtime-version=1.15 \
  --framework=scikit-learn \
  --python-version=3.7
```

Query the model



```bash
gcloud ai-platform predict \
  --model $model_name \
  --version $model_version \
  # The data we send to the prediction API
  --json_instances $input_file
```

## Lab: Using custom Containers with AI Platform Training

- 3 attempts to pass it

## [Quiz: Training, Tuning and Serving on AI Platform](quizzes/week2-3-training-tuning-and-serving-on-ai-platform.md.md)
