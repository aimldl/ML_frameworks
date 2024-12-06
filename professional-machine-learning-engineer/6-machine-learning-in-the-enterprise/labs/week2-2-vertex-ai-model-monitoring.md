# Lab: Vertex AI Model Monitoring

## Summary

- For details, refer to a Google Doc [Lab: Vertex AI Model Monitoring](https://docs.google.com/document/d/14mjk4rYDmaNOAkdxzkglaWNvOZrJz_WbR2yb-ITCYUo/edit#)

## Purpose

Model monitoring is the close tracking of the performance of ML models in production 

- so that production and AI teams can identify potential issues before they affect the business.

If production traffic differs from training data or varies substantially over time, 

- the quality of the answers your model produces is probably affected. 

When that happens, you will want to be alerted automatically and responsively 

- so that you can anticipate problems before they affect your customer experiences or your revenue streams.

### **What is Model Monitoring?**

You should be able to manage your ML services with the same degree of power and flexibility with which you can manage your applications. That's what **MLOps** is all about - managing ML services with the best practices Google and the broader computing industry have learned from generations of experience deploying well engineered, reliable, and scalable services. Model monitoring is a piece of the ML Ops puzzle **helps** **answer the following questions**:

- **training-serving skew**: How well do recent service requests match the training data used to build your model?
- **drift detection:** How significantly are service requests evolving over time?

Modern applications rely on a well established set of capabilities to monitor the health of their services. Examples include:

- software versioning
- rigorous deployment processes
- event logging
- alerting/notification of situations requiring intervention
- on-demand and automated diagnostic tracing
- automated performance and functional testing

## Learning objectives

- Deploy a pre-trained model.
- Configure model monitoring.
- Generate some artificial traffic.
- Interpret the data reported by the model monitoring feature.

## Setup and requirements

Enable

1. Navigation menu > API & Services > Library > Notebooks API
4. Navigation menu > API & Services > Library > Vertex AI API

## Task

1. Launch Vertex AI > Workbench
2. Clone a course repo within your Vertex AI Notebooks instance
   - git clone https://github.com/GoogleCloudPlatform/training-data-analyst

3. Monitor your Vertex AI model
   - [training-data-analyst > courses > machine_learning > deepdive2](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2) > [machine_learning_in_the_enterprise > **labs**](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2/machine_learning_in_the_enterprise/labs) > [**model_monitoring.ipynb**](https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive2/machine_learning_in_the_enterprise/labs/model_monitoring.ipynb)
   - [training-data-analyst > courses > machine_learning > deepdive2](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2) > [machine_learning_in_the_enterprise > **solutions**](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2/machine_learning_in_the_enterprise/solutions) > [**model_monitoring.ipynb**](https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive2/machine_learning_in_the_enterprise/solutions/model_monitoring.ipynb)
4. Cleanup
