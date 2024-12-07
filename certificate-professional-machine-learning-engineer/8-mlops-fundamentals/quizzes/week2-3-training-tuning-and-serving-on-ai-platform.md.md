# Quiz: Training, Tuning and Serving on AI Platform

**100%**

Question 1

Which command allows you to split your dataset to get 70% of it for training in a repeatable fashion?

- [ ] RAND() < 0.7
- [ ] REPEAT(RAND() < 0.7)
- [ ] MOD(RAND() < 0.7)
- [x] MOD(ABS(FARM_FINGERPRINT(field)),10) < 7



Question 2

Hyperparameter tuning happens before model training and is the task responsible for assigning initial weights to the variables (or parameters) which allow the model to find patterns on the data.

- [ ] True
- [x] False



Question 3

Which of the following is an INCORRECT statement about Dockerfile commands?

- [ ] The FROM command should be the first command in a Dockerfile file.
- [x] The ENTRYPOINT command specifies the name of the container so it can be found in the Container Registry.
- [ ] The RUN statement, followed by standard bash code, is used to provision the image with all the tools and libraries needed to run the training code.
- [ ] The WORKDIR command specifies what the current working directory should be when the container is executed.

```markdown
In gemeral, the 3rd one is not true in general. The RUN statement runs some commands. For this example specifically, provision the image and so on.
```



Question 4

What is the order of steps to push a trained model to AI Platform for serving?

I - Run the command gcloud ai-platform versions create {model_version} to create a version for the model.

II - Train and save the model.

III - Run the command gcloud ai-platform models create to create a model object.

IV - Run the command gcloud ai-platform predict to get predictions.

- [x] II, III, I, IV
- [ ] I, II, III, IV
- [ ] III, II, IV, I 
- [ ] II, I, III, IV 
