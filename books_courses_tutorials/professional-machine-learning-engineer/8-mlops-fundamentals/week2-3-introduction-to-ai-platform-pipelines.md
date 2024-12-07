# Week2-3-Introduction to AI Platform Pipelines

- Nitin Aggarwal

## Overview

Making AI



Few common AI problems



1 Kubeflow/TFX scalable ML services on Kubernetes



2 Reusable pipelines



3 Ecosystem



Android ecosystem analogy



## Introduction to AI Platform Pipelines

What is an ML pipeline?



Understanding pipeline components



Understanding a pipeline workflow



Current process for building an MLOps pipeline



A new product was needed to deploy robust, repeatable machine learning pipelines along with monitorying, auditing, version tracking, and repdocubility and deliver an enterprise-ready, easy-to-install, secure execution environment for your ML workflows.

What is AI Platform Pipelins?



Two major parts of an AI Platform Pipelines instance



Key benefits of using AI Platform Pipelines

1 Easy installation



2 Easy Authentication process



## AI Platform Pipelines

### Concepts

AI Platform Pipelines tech stack



- MLMD (ML Metadata)
- Lineage = 혈통 (=ancestry) 

AI Platform Pipelines implementation strategy



Some features of AI Platform Pipelines

1. Build your own ML pipeline with TFX examples



2. Pipeline versioning



3. Artifact tracking





4. Lineage tracking



### When to Use?

What does AI Platform Pipelines enable?



Visual depiction of pipeline topology



Rich visualizations of metrics



Access to all config params, inputs, and outputs for each run



What constitutes an AI Platform Pipelines instance?



- Dataproc: Fully managed Spark & Hadoop services that can handle
  - batch
  - streaming
  - query

TFX + Kubeflow Pipelines



- pusher
  - TFX > [The Pusher TFX Pipeline Component](https://www.tensorflow.org/tfx/guide/pusher)
    - is used to push a validated model to a deployment target
      - during model training or re-training



Rapid, reliable experimentation



View all current and historical runs grouped as "Experiments"



Select any Run to see all params and metrics



Clone an existing pipeline





Share, re-use and compose



### Ecosystem

AI problems today



Reusable pipelines: Force multiplier for data scientists



- [Business logic](https://en.wikipedia.org/wiki/Business_logic), Wikipedia
  - In computer [software](https://en.wikipedia.org/wiki/Software), **business logic** or **domain logic** is the part of the program that encodes the real-world [business rules](https://en.wikipedia.org/wiki/Business_rule) that determine how data can be [created, stored, and changed](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete).  It is contrasted with the remainder of the software that might be concerned with lower-level details of managing a [database](https://en.wikipedia.org/wiki/Database) or displaying the [user interface](https://en.wikipedia.org/wiki/User_interface), system infrastructure, or generally connecting various parts of the program.
- [비즈니스 로직(Business Logic)이란?](https://mommoo.tistory.com/67)

Mission

- Google Cloud AI Hub
  - The one place for everything AI, from experimentation to production



AI Hub



AI Hub and Pipelines: Fast and simple adoption of AI



- flyweel = 떠 있는 바퀴, 성장을 만드는 선순환의 수레바퀴를 의미

