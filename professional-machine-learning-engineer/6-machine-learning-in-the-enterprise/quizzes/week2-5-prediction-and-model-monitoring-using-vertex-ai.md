# Quiz: Prediction and Model Monitoring Using Vertex AI

**Score: 83.33%** --> 
Question 1

Which statements are correct for serving predictions using Pre-built containers?


- [ ] Vertex AI provides Docker container images that you run as pre-built containers for serving predictions.

- [ ] Pre-built containers provide HTTP prediction servers that you can use to serve prediction using minimal configurations.

- [ ] Pre-built containers are organized by Machine learning framework and framework version.

- [x] All of the options are correct.


Question 2

Which statement is correct regarding the maximum size for a CSV file during batch prediction?


- [ ] The data source file must be no larger than 100 GB.

- [x] Each data source file must not be larger than 10 GB. You can include multiple files, up to a maximum amount of 100 GB.

- [ ] The data source file must be no larger than 50 GB. You can not include multiple files.

- [ ] Each data source file must include multiple files, up to a maximum amount of 50 GB.


Question 3

What should be done if the source table is in a different project?

```
This doesn't fully make sense to me.
```

- [x] You should provide the BigQuery Data Editor role to the Vertex AI service account in that project.

- [ ] You should provide the BigQuery Data Viewer role to the Vertex AI service account in that project.

- [ ] You should provide the BigQuery Data Editor role to the Vertex AI service account in your project. **(wrong guess)**

- [ ] You should provide the BigQuery Data Viewer role to the Vertex AI service account in your project.


Question 4

Which of the following statements is invalid for a data source file in batch prediction?
```
You must use a "multi-"regional BigQuery dataset.
```

- [ ] The first line of the data source CSV file must contain the name of the columns.

- [ ] If the Cloud Storage bucket is in a different project than where you use Vertex AI, you must provide the Storage Object Creator role to the Vertex AI service account in that project.

- [ ] BigQuery data source tables must be no larger than 100 GB.

- [x] You must use a regional BigQuery dataset.


Question 5

What are the features of Vertex AI model monitoring?
```
Review the full meaning of feature attribution.
```

- [ ] Drift in data quality

- [ ] Skew in training vs. serving data

- [x] Feature Attribution and UI visualizations

- [ ] All of the options are correct.


Question 6

For which, the baseline is the statistical distribution of the feature's values seen in production **in the recent past**.

- [ ] Categorical features

- [ ] Numerical features

- [x] Drift detection

- [ ] Skew detection

