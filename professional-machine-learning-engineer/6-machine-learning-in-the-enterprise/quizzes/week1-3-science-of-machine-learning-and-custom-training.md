# Quiz: Science of Machine Learning and Custom Training

**Your grade: 83.33%** --> **100%**
Question 1

**Model complexity** often refers to **the number of features or terms** included in a given predictive model. What happens when the complexity of the model increases?

```
The 1st & 2nd answers seem equal.The answer is 4. But I think the 3 is not correct. That's why I got confused with this question.
```

- [ ] Model is more likely to overfit.

- [ ] Model will not figure out general relationships in the data.

- [ ] Model performance on a test set is going to be poor.

- [x] All of the options are correct.


Question 2

The learning rate is a hyperparameter that controls how much to change the model in response to the estimated error each time the model weights are updated. Choosing the learning rate is challenging. What can happen if the value is too small?


- [x] Training may take a long time. 

- [ ] If the learning rate value is too small, then the model will diverge. 

- [ ] The model will train more quickly. 

- [ ] Smaller learning rates require less training epochs given the smaller changes made to the weights each update.


Question 3

The learning rate is a hyperparameter that controls how much to change the model in response to the estimated error each time the model weights are updated. Choosing the learning rate is challenging. What can happen if the value is too large?


- [ ] Training may take a long time. 

- [ ] If the learning rate value is too large, then the model will converge. 

- [ ] The model will not train.. 

- [x]  A large learning rate value may result in the model learning a sub-optimal set of weights too fast or an unstable training process.


Question 4

Which of the following is true?
```
It'll be educational to review this part again from the perspective of the question.
```

- [x] Larger batch sizes require smaller learning rates.

- [ ] Smaller batch sizes require smaller learning rates.

- [ ] Larger batch sizes require larger learning rates.

- [ ] Smaller batch sizes require larger learning rates.


Question 5

The learning rate is a configurable hyperparameter used in the training of neural networks that has a small positive value, often in the range between _______

- [ ]  1.0 and 3.0.

- [x]  0.0 and 1.0.

- [ ] \> 0.0 and < 1.00.
- [ ] < 0.0 and > 1.00.

Question 6

What is "data parallelism” in distributed training?

- [ ] Run the same model & computation on every device, but train each of them using the same training samples.

- [ ] Run different models & computation on every device, but train each of them using only one training sample.

- [x] Run the same model & computation on every device, but train each of them using different training samples.

- [ ] Run different models & computation on a single device, but train each of them using different training samples.
