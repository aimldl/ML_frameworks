# Feature Engineering

* Draft: 2022-11-27 (Sun)

## Course Introduction

Want to know about Vertex AI Feature Store? Want to know how you can  improve the accuracy of your ML models? What about how to find which  data columns make the most useful features? 

Welcome to Feature  Engineering, where we discuss good versus bad features and how you can  preprocess and transform them for optimal use in your models. This  course includes content and labs on feature engineering using BigQuery  ML, Keras, and TensorFlow.

## Dataflow and Apache Beam

```
Google Cloud Dataflow is a fully managed service for executing Apache Beam pipelines within the Google Cloud Platform ecosystem
```

Dataflow = managed service for Apache Beam

- Apache Beam
  - Beam come from a contraction of batch and stream.
    - b(atch+str)eam
    - beam = batch + stream

### Data source/sink

The destination of the pipeline is called a sink.

#### Examples of data source

- batch data source : Google Cloud Storage
  - e.g. The lines could come from a file in Google Cloud Storage.
- streaming data source : Pub/sub

#### Examples of data sink

- batch data destination : Google Cloud Storage
- streaming data destination : Pub/sub
- BigQuery

### Implementation

The following Implementation separates 

- the pipeline definition 
- from the pipeline execution.

#### Sample Python code

```python
p = beam.Pipeline()
( p
	|
	...
)
p.run();
```

- `|` is a pipeline.
- The pipeline is defined in `( p |... )`
- p.run()
  - The pipeline get executed only when you call the `run` method.

### Advantage of Dataflow

- A fully managed offering from Google allows you to 
  - execute data processing pipelines at scale.
- Dataflow can change the amount of computing resources.
  - You don't have to worry about managing the size of the cluster that runs your pipeline.
  - The number of servers that will run your pipeline elastically changes
    - depending on the amount of data that your pipeline is to process.
- You can use the same pipeline logic 
  - for both batch and streaming data sources.
  - for both batch and streaming data destinations.
- You can easily change the destination source/destination without changing the logic of your pipeline implementation.

## Terminologies

- PCollection
  - is a data structure with pointers
    - where the Dataflow cluster stores your data.
    - That's how Dataflow can provide elastic scaling of the pipeline.
  - does not store all of its data in memory (unlike many data structures).
- runners
  - Apache Spark
  - Direct runner (=local computer)
  - Customer runner (=your own distributed computing platform)

- Transform

The following part is taken from Coursera > Feature Engineering > "".

#### Apply Transform to PCollection

- Data in a pipeline are represented by PCollection.
- Supports parallel processing
- Not an in-memory collection; can be unbounded

```
lines = p | ...
```

Apply Transform to PCollection; return PCollection.

```
sizes = lines | 'Length' >> beam.Map(lambda line: len(line) )
```

#### Ingesting data into a pipeline (Python)

- Read data from file system, Cloud Storage or BigQuery
- Text formats return String

```
lines = beam.io.ReadFromText('gs://.../input-*.csv.gz')
```

BigQuery returns a TableRow

```
rows = beam.io.Read( beam.io.BigQuerySource(query='SELECT x,y,z' \
               'FROM [project:dataset.tablename]', project='PROJECT') )
```

#### Can write data out to same formats (Python)

Write data to file system, Cloud Storage or BigQuery

```
beam.io.WriteToText( file_path_prefix='/data/output', file_name_suffix='.txt')
```

Can prevent sharding of output (do only if it is small)

```
beam.io.WriteToText( file_path_prefix='data/output', file_name_suffix='.txt',
                     num_shards = 1)
```

The output must be a PCollection of Strings before writing out

#### Executing pipeline (Python)

Simply running main()runs pipeline locally

```bash
python ./grep.py
```

To run on cloud, specify cloud parameters and submit the job to Dataflow

```bash
python ./grep.py \
	--project=$PROJECT \
	--job_name=myjob \
	--staging_location=gs://$BUCKET/staging/ \
	--temp_location=gs://$BUCKET/staging/ \
	--runner=DataflowRunner
```

