# Lab: CI/CD for a Kubeflow Pipeline

- 2 hours
- https://www.coursera.org/learn/mlops-fundamentals/ungradedLti/ANhzI/ci-cd-for-a-kubeflow-pipeline

```markdown
The difference between this lab & the previous lab is the notebooks!

- The first part is exactly the same.
- Deploy Kubeflow Pipelines
- Launch Vertex Workbench
- Open JupyterLab
- Git clone the course repo.
```

## Note

- This lab is incomplete due to errors included in the lab material.
- Go to TODOs for details.

## Purpose

- Authoring of a Cloud Build CI/CD workflow
  - that automatically builds and deploys a Kubeflow Pipeline (KFP). 

- Integrate your workflow with GitHub 
  - by **setting up a trigger** that starts the workflow 
    - when a new tag is applied to the GitHub repo hosting the pipeline's code.

## Learning objectives

- Create a **custom** <u>Cloud Build builder</u> 
  - to pilote CAIP Pipelines
- Write a Cloud Build **config file** 
  - to build and push all the artifacts for a KFP
- Setup a Cloud Build **Github trigger** 
  - to rebuild the KFP

## Related Files 

Google docs

- [Lab: CI/CD for a Kubeflow Pipeline](https://docs.google.com/document/d/19R8cSotw9T9kma8xzNI4_rsioEVUOSACE7wua6NNuHU/edit#heading=h.clc569hxwadr)

## TODO

### A command fails to run due to Python package dependency issue.

```bash
!gcloud builds submit . --config cloudbuild.yaml --substitutions {SUBSTITUTIONS}
```

```bash
  ...
  Step #0: ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
Step #0: visions 0.7.5 requires pandas>=0.25.3, but you have pandas 0.24.2 which is incompatible.
  ...
ERROR: failed to pull because we ran out of retries.
  ... 
BUILD FAILURE: Build step failure: build step 2 "gcr.io/qwiklabs-gcp-02-30335f9a60d4/kfp-cli" failed: error pulling build step 2 "gcr.io/qwiklabs-gcp-02-30335f9a60d4/kfp-cli": generic::unknown: retry budget exhausted (10 attempts): step exited with non-zero status: 1
ERROR: (gcloud.builds.submit) build e2d88103-64f8-419c-aacb-2a2cfc358826 completed with status "FAILURE"
$
```

- A newer Pandas version is necessary.
- **TODO: Figure out where to fix this config and run the following command again.**

#### Hint

```python
SUBSTITUTIONS="""
  ...
_PIPELINE_PACKAGE=covertype_training_pipeline.yaml,\
```

I was looking for the above yaml file, but it was not in any sub-directories.

```bash
$ cd ~/mlops-on-gcp/on_demand/kfp-caip-sklearn/lab-03-kfp-cicd
$ tree
.
├── README.md
├── base_image
│   └── Dockerfile
├── cloudbuild.yaml
├── exercises
│   ├── base_image
│   │   └── Dockerfile
│   ├── cloudbuild.yaml
│   ├── kfp-cli
│   │   └── Dockerfile
│   ├── lab-03.ipynb
│   ├── pipeline
│   │   ├── covertype_training_pipeline.py
│   │   └── helper_components.py
│   └── trainer_image
│   	├── Dockerfile
│   	└── train.py
├── kfp-cli
│   └── Dockerfile
├── lab-03.ipynb
├── pipeline
│   ├── covertype_training_pipeline.py
│   └── helper_components.py
└── trainer_image
	├── Dockerfile
	└── train.py

9 directories, 17 files
$
```

The closest file is [pipeline/covertype_training_pipeline.py](https://github.com/GoogleCloudPlatform/mlops-on-gcp/blob/master/on_demand/kfp-caip-sklearn/lab-03-kfp-cicd/pipeline/covertype_training_pipeline.py) which has a function. 

- Q: Does this function create the yaml file on the fly?
- A: No. It's to train the pipeline with the forest cover type dataset.

```python
@kfp.dsl.pipeline(
	name='Covertype Classifier Training',
	description='The pipeline training and deploying the Covertype classifierpipeline_yaml'
)
def covertype_train(project_id,
                	region,
                	source_table_name,
                	gcs_root,
                	dataset_id,
                	evaluation_metric_name,
                	evaluation_metric_threshold,
                	model_id,
                	version_id,
                	replace_existing_version,
                	hypertune_settings=HYPERTUNE_SETTINGS,
                	dataset_location='US'):
  """Orchestrates training and deployment of an sklearn model."""

  # Create the training split
  query = generate_sampling_query(
  	source_table_name=source_table_name, num_lots=10, lots=[1, 2, 3, 4])

  training_file_path = '{}/{}'.format(gcs_root, TRAINING_FILE_PATH)

  create_training_split = bigquery_query_op(
  	query=query,
  	project_id=project_id,
  	dataset_id=dataset_id,
  	table_id='',
  	output_gcs_path=training_file_path,
  	dataset_location=dataset_location)

  # Create the validation split
  query = generate_sampling_query(
  	source_table_name=source_table_name, num_lots=10, lots=[8])

  validation_file_path = '{}/{}'.format(gcs_root, VALIDATION_FILE_PATH)

  create_validation_split = bigquery_query_op(
  	query=query,
  	project_id=project_id,
  	dataset_id=dataset_id,
  	table_id='',
  	output_gcs_path=validation_file_path,
  	dataset_location=dataset_location)

  # Create the testing split
  query = generate_sampling_query(
  	source_table_name=source_table_name, num_lots=10, lots=[9])

  testing_file_path = '{}/{}'.format(gcs_root, TESTING_FILE_PATH)

  create_testing_split = bigquery_query_op(
  	query=query,
  	project_id=project_id,
  	dataset_id=dataset_id,
  	table_id='',
  	output_gcs_path=testing_file_path,
  	dataset_location=dataset_location)

  # Tune hyperparameters
  tune_args = [
  	'--training_dataset_path',
  	create_training_split.outputs['output_gcs_path'],
  	'--validation_dataset_path',
  	create_validation_split.outputs['output_gcs_path'], '--hptune', 'True'
  ]

  job_dir = '{}/{}/{}'.format(gcs_root, 'jobdir/hypertune',
                          	kfp.dsl.RUN_ID_PLACEHOLDER)

  hypertune = mlengine_train_op(
  	project_id=project_id,
  	region=region,
  	master_image_uri=TRAINER_IMAGE,
  	job_dir=job_dir,
  	args=tune_args,
  	training_input=hypertune_settings)

  # Retrieve the best trial
  get_best_trial = retrieve_best_run_op(project_id, hypertune.outputs['job_id'])

  # Train the model on a combined training and validation datasets
  job_dir = '{}/{}/{}'.format(gcs_root, 'jobdir', kfp.dsl.RUN_ID_PLACEHOLDER)

  train_args = [
  	'--training_dataset_path',
  	create_training_split.outputs['output_gcs_path'],
  	'--validation_dataset_path',
  	create_validation_split.outputs['output_gcs_path'], '--alpha',
  	get_best_trial.outputs['alpha'], '--max_iter',
  	get_best_trial.outputs['max_iter'], '--hptune', 'False'
  ]

  train_model = mlengine_train_op(
  	project_id=project_id,
  	region=region,
  	master_image_uri=TRAINER_IMAGE,
  	job_dir=job_dir,
  	args=train_args)

  # Evaluate the model on the testing split
  eval_model = evaluate_model_op(
  	dataset_path=str(create_testing_split.outputs['output_gcs_path']),
  	model_path=str(train_model.outputs['job_dir']),
  	metric_name=evaluation_metric_name)

  # Deploy the model if the primary metric is better than threshold
  with kfp.dsl.Condition(
  	eval_model.outputs['metric_value'] > evaluation_metric_threshold):
	deploy_model = mlengine_deploy_op(
    	model_uri=train_model.outputs['job_dir'],
    	project_id=project_id,
    	model_id=model_id,
    	version_id=version_id,
    	runtime_version=RUNTIME_VERSION,
    	python_version=PYTHON_VERSION,
    	replace_existing_version=replace_existing_version)
 
  # Configure the pipeline to run using the service account defined
  # in the user-gcp-sa k8s secret
  if USE_KFP_SA == 'True':
	kfp.dsl.get_pipeline_conf().add_op_transformer(use_gcp_secret('user-gcp-sa'))
```



### Integrate your CI/CD workflow with **GitHub**

- This was not done because of the previous error.
- It looks like github charges for the trigger functionality.
  - **TODO: Check this out.**



- Use [Cloud Build GitHub App or https://github.com/marketplace/google-cloud-build](https://github.com/marketplace/google-cloud-build)

- Set up a trigger that starts the CI/CD workflow 

- - when a new tag is applied to the **GitHub** repo

- Use a fork of this repo as your source GitHub repository.
