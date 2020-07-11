# Apache Beam Pipeline for Cleaning Batch Data Using Cloud Dataflow and BigQuery
Apache Beam is an open-source, unified model for constructing both batch and streaming data processing pipelines. Beam supports multiple language-specific SDKs for writing pipelines against the Beam Model such as Java, Python, and Go and Runners for executing them on distributed processing backends, including Apache Flink, Apache Spark, Google Cloud Dataflow and Hazelcast Jet.

We are going to create a pipeline that cleans the data for making it analysis ready using apache beam (Python SDK), and run it using dataflow runner. Here we are going to use Craft Beers Dataset from Kaggle.

https://www.kaggle.com/nickhould/craft-cans

## Basic flow of the pipeline 

1. Read the data from google cloud storage bucket (Batch). 
2. Create a cleaning pipeline using Apache Beam.
3. Run it using Dataflow runner (Dataflow). 
4. Write the data into data Sink (BigQuery) and analyze it.
5. Create beautiful visualization (Data Studio).
