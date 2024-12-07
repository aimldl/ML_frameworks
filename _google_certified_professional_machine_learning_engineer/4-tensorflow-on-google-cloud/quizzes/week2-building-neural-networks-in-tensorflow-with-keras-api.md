# Quiz: Building Neural Networks in TensorFlow with Keras API

Q1. Non-linearity helps in training your model at a much faster rate and with more accuracy without the loss of your important information?

```
Q: Training your model at a much faster rate?
With linearity, a model can't be learned. Non-linearity helps fitting the model, but not sure if it expedites the model training.
```

- **True**
- False **[wrong guess]**

Q2. During the training process, each additional layer in your network can successively reduce signal vs. noise. How can we fix this?

```
Q: What does it mean by "successively reduce signal vs. noise"?
   Reducing the signal-to-noise ratio (which is not good)?
```

- Use non-saturating, linear activation functions.

- **Use non-saturating, nonlinear activation functions such as ReLUs.** **[correct guess]**
- 
  Use sigmoid or tanh activation functions.

- None of the options are correct.

Q3. How does Adam (optimization algorithm) help in compiling the Keras model?

- By updating network weights iteratively based on training data

- 
  By diagonal rescaling of the gradients

- **Both by updating network weights iteratively based on training data by diagonal rescaling of the gradients**
- None of the options are correct.

[Keras API reference](https://keras.io/api) / [Optimizers](https://keras.io/api/optimizers) / [Adam](https://keras.io/api/optimizers/adam/)

Adam optimization is a **stochastic gradient descent** method that is based on **adaptive estimation of first-order and second-order moments**.

According to [Kingma et al., 2014](http://arxiv.org/abs/1412.6980), the method is "***computationally efficient, has little memory requirement, invariant to diagonal rescaling of gradients, and is well suited for problems that are large in terms of data/parameters***".

Q4. The predict function in the tf.keras API returns what?

- **Numpy array(s) of predictions**
- 
  Input_samples of predictions

- 
  Both numpy array(s) of predictions & input_samples of predictions

- 
  None of the options are correct.

Q5. What is the significance of the Fit method while training a Keras model?

```
At the first sight, none of them seems the correct answer.
```

- Defines the number of steps per epochs

- **Defines the number of epochs** [correct guess]
- 
  Defines the validation steps

- 
  Defines the batch size

Q6. Select the correct statement regarding the Keras Functional API.

- Unlike the Keras Sequential API, we do not have to provide the shape of the input to the model.

- **Unlike the Keras Sequential API, we have to provide the shape of the input to the model.**
- 
  The Keras Functional API does not provide a more flexible way for defining models.

- 
  None of the options are correct.

Q7. The Keras Functional API can be characterized by having:

- **Multiple inputs and outputs and models with shared layers.**
- 
  Single inputs and outputs and models with shared layers.

- 
  Multiple inputs and outputs and models with non-shared layers.

- 
  None of the options are correct.

Q8. How does regularization help build generalizable models ?

- **By adding dropout layers to our neural networks**
- 
  By using image processing APIS to find out accuracy

- 
  By adding dropout layers to our neural networks and by using image processing APIS to find out accuracy

- 
  None of the options are correct.

Q9. The L2 regularization provides which of the following?

- It subtracts a sum of the squared parameter weights term to the loss function.

- 
  It multiplies a sum of the squared parameter weights term to the loss function.

- **It adds a sum of the squared parameter weights term to the loss function.**
- 
  None of the options are correct.
