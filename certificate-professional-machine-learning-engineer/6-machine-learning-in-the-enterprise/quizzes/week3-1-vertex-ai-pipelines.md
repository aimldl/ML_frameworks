# Quiz: Vertex AI Pipelines

Your score: 75%
Question 1

Which package is used to define and interact with pipelines and components?
```
What is DSL in kfp?
dsl. pipeline is a decorator for Python functions that returns a pipeline. kfp. dsl. python_component is a decorator for Python functions that adds pipeline component metadata to the function object.2022. 9. 15.

Introduction to the Pipelines SDK - Kubeflow
https://www.kubeflow.org/docs/components/pipelines/v1/sdk/sdk-overview/

kfp.dsl contains the domain-specific language (DSL) that you can use to define and interact with pipelines and components.
```

- [ ] kfp.components (wrong guess)

- [x] kfp.dsl package

- [ ] kfp.compiler

- [ ] kfp.containers


Question 2

How can you define the pipeline's workflow as a graph?
```
What confusing here is to choose either
- pipeline
- component?
```

- [ ] By using different inputs for each component.

- [ ] Use the previous pipeline's output as an input for the current pipeline.

- [x] By using the outputs of a component as an input of another component

- [ ] By using predictive input for each component.


Question 3

What can you use to compile the pipeline?
```
Hmm...
```

- [ ] compiler.Compiler

- [ ] kfp.v2.compiler

- [ ] kfp.Compiler

- [x] kfp.v2.compiler.Compiler


Question 4

What can you use to create a **pipeline run** on Vertex AI Pipelines?


- [ ] Pipeline root path

- [ ] Service account

- [x] Vertex AI python client (guess)

- [ ] kfp.v2.compiler.Compiler