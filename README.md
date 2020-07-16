# Apache Beam Pipeline for Cleaning Batch Data Using Cloud Dataflow and BigQuery
Apache Beam is an open-source, unified model for constructing both batch and streaming data processing pipelines. Beam supports multiple language-specific SDKs for writing pipelines against the Beam Model such as Java, Python, and Go and Runners for executing them on distributed processing backends, including Apache Flink, Apache Spark, Google Cloud Dataflow and Hazelcast Jet.

We are going to create a pipeline that cleans the data for making it analysis ready using apache beam (Python SDK), and run it using dataflow runner. Here we are going to use Craft Beers Dataset from Kaggle.

https://www.kaggle.com/nickhould/craft-cans

## Basic flow of the pipeline 

1. Read the data from google cloud storage bucket (Batch). 
2. Apply some transformations such as splitting data by comma separator, dropping unwanted columns, convert data types, etc.
3. Write the data into data Sink (BigQuery) and analyze it.

You can see complete explaination of each benchmark in article given below:

https://medium.com/@aniketghole88/apache-beam-pipeline-for-cleaning-batch-data-using-cloud-dataflow-and-bigquery-f9272cd89eba
