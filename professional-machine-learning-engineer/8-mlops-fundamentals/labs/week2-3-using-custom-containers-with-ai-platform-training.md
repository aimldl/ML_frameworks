# Lab: Using custom containers with AI Platform Training

- 2 hours
- https://www.coursera.org/learn/mlops-fundamentals/gradedLti/Trkja/qwiklabs-using-custom-containers-with-ai-platform-training

## Purpose

- Develop **a multi-class classification model**
  - **predicts the type of forest** cover from cartographic data
  - **Covertype Data Set** from UCI Machine Learning Repository.
  - **Scikit-learn + hyperparam tuning**
- Package the model as a docker image
- Run on AI Platform Training as a training application.

## Learning objectives

- Create a train and a validation **split with Big Query**
- Wrap a machine learning model into **a Docker container** and train it on AI Platform
- Use the **hyperparameter tunning engine** on GCP to find the best hyperparameters
- **Deploy** a trained machine learning model GCP **as a REST API** and query it

## Related Files 

Google docs

- [Lab: Using custom containers with AI Platform Training](https://docs.google.com/document/d/1cTqBW4kcAWiiweG7gFCOqFAjL5j5LnmbZA2xaMY2ZuY/edit#)
  - [CLI > Cloud Shell > Introduction](https://docs.google.com/document/d/1jueCxZaQB1gObqXOx0gCWq7AqEsRSDN6YpUBrFzxnbA/edit#heading=h.2sws9c4vhvpb)
  - [CLI > Enable Cloud Services](https://docs.google.com/document/d/1PlrwxvQiikeD96HHICogWZGYmozNIYoRyKG1lq8a2I8/edit#heading=h.ucf98emwfqz)
  - [Prepare AI Platform Pipelines instance](https://docs.google.com/document/d/1pLLq0_YHQFEqzganDERtCKuLWsoW4ikaopZp9NmHJKo/edit#)

Notebooks

- [lab-01-1_clear_all_outputs.ipynb](ipynb_files/lab-01-1_clear_all_outputs.ipynb)
- [lab-01-2_I_didn't_pass_the_last_two_tasks.ipynb](ipynb_files/lab-01-2_I_didn't_pass_the_last_two_tasks.ipynb)
