# Quiz: Designing adaptable ML systems

**71.42%** --> **85.71%** -->**100%**

Hmm... It took about 50 mins to complete this quiz. 



Question 1

Which of the following models are **susceptible to a feedback loop**? Check all that apply.

```
Check out the logic AFTER the choices.
```

- [x] A university-ranking model that rates schools in part by their **selectivity (the percentage of students who applied that were admitted)**.
- [x] A book-recommendation model that suggests novels its users may like based on their popularity (i.e., the number of times the books have been purchased).
- [ ] An election-results model that forecasts the winner of a mayoral race by surveying 2% of voters after the polls have closed. **(should've be unchecked!)**
- [x] A traffic-forecasting model that predicts congestion at highway exits near the beach, using beach crowd size as one of its features.
- [ ] A face-attributes model that detects whether a person is smiling in a photo, which is regularly trained on a database of stock photography that is automatically updated monthly.
- [ ] A housing-value model that predicts house prices, using size (area in square meters), number of bedrooms, and geographic location as features. **(should've be unchecked!)**

### 

**A university-ranking model**

- The model's rankings may drive additional interest to top-rated schools, increasing the number of applications they receive. If these schools continue to admit the same number of students, **selectivity will increase** (the percentage of students admitted will go down). **This will boost these schools' rankings, which will further increase prospective student interest, and so on…**

A book-recommendation model

- Book recommendations are likely to drive purchases, and these additional sales will be fed back into the model as input, **making it more likely to recommend these same books in the future**.

An election-results model

-  If the model does not publish its forecast until after the polls have closed, its predictions cannot affect voter behavior.
- -> Come on! It's obvious who will be the major after the vote. And by the time the next prediction is needed, we know who was the major.
  - Additionally, how can you guarantee 2% of sample enough and unbiased to represent the set?

A face-attributed model

- (This is not the commented by Coursera.) I think the regular update mechanism makes the model robust compared to other cases.

A housing-value model

- **A house's location, size, or number of bedrooms cannot be quickly changed** in response to price forecasts, which makes a feedback loop unlikely. However, there is potentially a correlation between size and number of bedrooms (larger homes are likely to have more rooms) that may need to be analyzed.
- Well, in my opinion, the economic situation changes over time which is reflected to the housing price. I guess the person who made this question & answer may not have lived in a mega-city like my city. I feel an important feature is missing.



Question 2

Suppose you are building an ML-based system to predict the likelihood that a customer will leave a positive review. **The user interface that customers leave reviews on changed a few months ago, but you don't know about this.** Which of these is a potential consequence of mismanaging this data dependency?

```
model serving signature?
특징
 signature
    1. Noun 서명
    2. Noun 격식 서명(하기)
    3. Noun 특징 (→digital signature, key signature, time signature)

- 모델 제공 서명 is wrong.
```



- [x] Losses in prediction quality
- [ ] Change in ability of model to be part of a streaming ingest
- [ ] Change in **model serving signature**

### 

Question 3

What is **training skew** caused by?



- [ ] The Cloud Storage you load your data from in the training environment is physically closer than the Cloud Storage you load your data from in the production environment.
- [ ]  The prediction environment is slower than the training environment. 
- [ ] Starting and stopping of the processing when training the model.
- [x] Your development and production **environments are different, or different code** is used in the training environment than in the development environment.

### 

Question 4

**Gradual drift** is used for which of the following?

```
1 & 2 are sudden drift; 4 is recurring drift
```

- [What Is Concept Drift And Why Does It Go Undetected?](https://censius.ai/blogs/what-is-concept-drift-and-why-does-it-go-undetected)

- [How Concept Drift Ruins Your Model Performance](https://towardsdatascience.com/concept-drift-can-ruin-your-model-performance-and-how-to-address-it-dff08f97e29b)

- [ ] A new concept that occurs within a short time
- [ ] A new concept that rapidly replaces an old one over a short period of time 
- [x] An old concept that incrementally changes to a new concept over a period of time
- [ ] An old concept that may reoccur after some time

### 

Question 5

Which of the following tools help software users manage dependency issues?

- [ ] Modular programs **(wrong answer)**
- [ ] Maven, Gradle, and Pip
- [ ] Monolithic programs
- [ ] Polylithic programs **(wrong answer)**

```
Polylithic programs

Polylithic design
https://infovis-wiki.net/wiki/Polylithic_design

Generally, a polylithic design is given when a software provides a high count of different classes. Each class provides only a small amount of functionality. These separated classes are consolidated through several programming techniques like inheritance or generic concepts.

A lot of separation allow developers to change or manipulate existing functionality selectively. Furthermore, a high abstraction of objects forces developer to implement well thought out components which may also work correctly when other components have changed. Typically, this results in a clear, flexible, and elaborate architecture. Furthermore, the code of single classes is less complex.

Nevertheless, the large count of objects may also lead to unconsidered mistakes and makes it harder to understand the software. Furthermore, the separation between objects can exceed a normal dimension. In case of too many classes developers will have problems in conceiving the whole architecture. Especially generic concepts (e.g., reflection) must be applied very carefully as external developers often have no insight in such concepts.

In visualization, especially the separation between abstract data, visual structures, and rendering routines is defined as polylithic design.

See also: monolithic design 

Monolithic design
https://infovis-wiki.net/wiki/Monolithic_design
Generally, a monolithic design is given when a software provides its functionality centralised in one or just a few classes. Such classes are very powerful and typically easy to apply.

Such a design does not need a complex architecture with a deep class structure through inheritances. Developer typically will not have troubles to conceive the software as only a few elements must be studied in detail (exept the top-level class is very complex). Further, such an approach typically ensures fast results when applying the software. This is obtained as such implementations typically do not provide excessive functionality, instead, they are specialized on a limited count of features that may be applied easily.

However, in case of providing a lot of functionality such an approach may lead to unclear or sleazy code as there is no clear separation to other areas of the software. Further, it is hard to manipulate or change existing code, also extensions may be hard to realize. So, developers are well advised to implement more flexible code when a certain dimension of functionality is reached.

In visualization a software is called monolithic when abstract data, visual structures, and rendering routines are not separated explicity.

See also: polylithic design 
```

```
Ah, OK. Dependency issues (of packages!)

Maven is for Java
Gradle is for DSL (Domain-Specific Language)
Pip is for Python.

What is Gradle? Why Do We Use Gradle? Explained
https://www.simplilearn.com/tutorials/gradle-tutorial/what-is-gradle
- Build automation tool
  - The build process become more consistent with the help of build automation tools.
- The build process = compiling, linking & packaging the code.
```





Question 6

Which component identifies anomalies in training and serving data and can **automatically create a schema** by examining the data?

```
TFX > TFDV  includes tools for
- statistics
- schema
- anomalies

https://www.tensorflow.org/tfx/data_validation/get_started
- TFX (TensorFlow Extended)
- TF Data Validation (TFDV)
```



- [ ] Data ingestion

- [ ] Data transform

- [x] Data validation

- [ ] Data identifier

  

Question 7

What is the shift in the actual relationship between the model inputs and the output called?



- [ ] Data drift
- [x] Concept drift
- [ ] Prediction drift
- [ ] Label drift
