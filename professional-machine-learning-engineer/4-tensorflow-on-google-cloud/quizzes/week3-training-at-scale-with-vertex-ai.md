# Quiz: Training at Scale with Vertex AI

Q1. Fill in the blanks. When sending training jobs to Vertex AI, it is common to split most of the logic into a _________ and a ___________ file.

- **task.py, model.py**
- 
  task.json, model.json

- 
  task.avro, model.avro

- 
  task.xml, model.xml

Q2. Which file is the entry point to your code that Vertex AI will start and contains details such as “how to parse command-line arguments and where to write model outputs?

- model.py

- 
  tmodel.json

- 
  tmodel.avro

- **task.py**

Q3. When you package up a TensorFlow model as a Python Package, what statement should every Python module contain in every folder?

- model.py

- 
  tmodel.json

- 
  tmodel.avro

- **an init_.py**

Q4. To make your code compatible with Vertex AI, there are three basic steps that must be completed in a specific order. Choose the answer that best describes those steps.

- First, upload data to Google Cloud Storage. Then submit your training job with gcloud to train on Vertex AI. Next, move code into a trainer Python package. 

- 
  First, download data from Google Cloud Storage. Then submit your training job with gcloud to train on Vertex AI. Next, move code into a trainer Python package. 

- 
  First, upload data to Google Cloud Storage. Next, move code into a trainer Python package. Then submit your training job with gcloud to train on Vertex AI.

- 
  First, move code into a trainer Python package. Next, upload data to Google Cloud Storage. Then submit your training job with gcloud to train on Vertex AI.

Q5. Fill in the blanks. You can use either pre-built containers or custom containers to run training jobs. Both containers require you specify settings that Vertex AI needs to run your training code, including __________, ____________, and ________.

- Source distribution name, job name, worker pool

- 
  Region, source distribution, custom URI

- **Region, display-name, worker-pool-spec**
- 
  Cloud storage bucket name, display-name, worker-pool-spec
