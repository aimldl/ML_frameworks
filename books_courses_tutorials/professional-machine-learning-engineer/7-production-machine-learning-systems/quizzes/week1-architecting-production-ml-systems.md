# Quiz: Architecting production ML systems

Score: 87:50%

Question 1

What percent of system code does the ML model account for?



- [x] 5%
- [ ] 25%
- [ ] 50%
- [ ] 90%



Question 2

Match the three types of data ingest with an appropriate source of training data.



- [x] Streaming (Pub/Sub), structured batch (BigQuery), unstructured batch (Cloud Storage)
- [ ] Streaming (BigQuery), structured batch (Pub/Sub), unstructured batch (Cloud Storage)
- [ ] Streaming batch (Dataflow), structured batch (BigQuery), stochastic (App Engine)



Question 3

What is the responsibility of **model evaluation and validation** components?



- [ ] To ensure that the models are not good before moving them into **a staging environment**.
- [ ] To ensure that the models are not good after moving them into a staging environment.
- [x] To ensure that the models are good before moving them into **a production/staging environment**.
- [ ] To ensure that the models are good after moving them into a production/staging environment.



Question 4

Which type of training do you use if your data set doesn’t change over time?



- [x] Static training
- [ ] Online training
- [ ] Dynamic training
- [ ] Real-time training



Question 5

Which type of logging should be enabled in the **online prediction** that logs the stderr and stdout streams from your prediction nodes to **Cloud Logging** and can be useful for debugging?

- [x] Container logging
- [ ] Cloud logging
- [ ] Access logging
- [ ] Request-response logging **(wrong guess)**

```
I think this was not covered in the videos.
```

Vertex AI > Doc. > Guides > [Online prediction logging](https://cloud.google.com/vertex-ai/docs/predictions/online-prediction-logging?hl=ko#enable_disable_logs-console)

- [Types of prediction logs](https://cloud.google.com/vertex-ai/docs/predictions/online-prediction-logging#log-types)
  - To Cloud Logging
    - **Container logging**
      - logs **the stdout and stderr streams from your prediction nodes** to Cloud Logging. 
      - These logs are essential and required for debugging.
    - **Access logging**
      - logs information like **timestamp and latency for each request** to Cloud Logging.
  - To BigQuery table
    - **Request-response logging** 
      - logs **a sample of online prediction requests and responses** to a BigQuery table.
      - You can enable request-response logging by creating or patching the prediction endpoint.

Question 6

Vertex AI has a unified data preparation tool that supports **image, tabular, text, and video content**. Where are uploaded datasets stored in Vertex AI?



- [ ] A Google Cloud Storage bucket that acts as an output for both AutoML, custom training jobs, serialized training jobs.
- [ ] A Google Cloud database that acts as an output for both AutoML and custom training jobs.
- [ ] A Google Cloud database that acts as an input for both AutoML and custom training jobs.
- [x] A Google Cloud Storage bucket that acts as an input for both AutoML and custom training jobs.



Question 7

In the featurestore, the timestamps are **an attribute of the feature values**, not a separate resource type.

```
I'm not 100% sure.
```



- [x] True
- [ ] False



Question 8

When you use the data to train a model, Vertex AI **examines the source data type and feature values** and infers how it will use that feature in model training. This is called the ________________for that feature.



- [ ] Transmutation
- [ ] Translation
- [x] Transformation
- [ ] Duplication

