

# 2 Introduction to TensorFlow Extended

TODO: double-check the contents.



## Interactive Pipelines



```python
import tensorflow as tf
from tfx.orchestration.experimental.interactive.interactive_context import InteractiveContext

context = InteractiveContext()
```

Set up your pipeline component(s)

```python
from tfx.components import StatisticsGen

statistics_gen = StatisticsGen(
  examples=example_gen.outputs['examples])
context.run(statistics_gen)

context.show(statistics_gen.outputs['statistics']

for artifact in statistics_gen.outputs['statistics'].get():
    print(artifact.uri)
```

Set up your pipeline component(s)

## Introduction to Apache Beam



### basic_pipeline.py

```python
import re

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

input_file = 'gs://dataflow-samples/shakespeare/kinglear.txt'
output_file = '/tmp/output.txt'

# Define pipeline options object
pipeline_options = PipelineOptions()

with beam.Pipeline(options=pipeline_options) as p:
    # Read the text file or file pattern into a PCollection.
    lines = p | ReadFromText(input_file)
    
# Count the occurrences of each word
count = {
    lines
    | 'Split' >> beam.FlatMap(lambda x: re.findall(r'[A-Za-z\']+', x))
    | 'PairWithOne' >> beam.Map(lambda x: (x,1))
    | 'GroupdAndSum' >> beam.CombinePerKey(sum))
    
# Format the counts into a PCollection of strings
def format_result(word_counts):
    (word, count) = word_count
    return "{}: {}".format(word, count)
    
output = counts | 'Format' >> beam.Map(format_result)

# Write the output using a 'Write' transform that has side effects
output | WriteToText(output_file)
```

Executing Your Basic Pipeline

```bash
$ python basic_pipeline.py
```

