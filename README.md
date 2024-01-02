# Spotify Data Engineering Project

## Overview

This project demonstrates a complete data pipeline for extracting, transforming, and loading Spotify data. The process involves integrating with the Spotify API, deploying code on AWS Lambda for data extraction, setting up triggers for automatic execution, transforming data, storing files on AWS S3, and building analytics tables using AWS Glue and Athena.

## Project Structure

- **`lambda_function.py`**: Contains the AWS Lambda function code for extracting data from the Spotify API.
- **`transform.py`**: Includes the transformation function to process the raw data.
- **`glue_script.py`**: AWS Glue script for defining and running ETL jobs.
- **`analytics_tables.sql`**: SQL script to create analytics tables in Athena.

## Instructions

### 1. Extracting Data with AWS Lambda

- Deploy the code in `lambda_function.py` to AWS Lambda.
- Set up environment variables for Spotify API credentials.
- Configure an automatic trigger (e.g., CloudWatch Events) for periodic execution.

### 2. Transforming Data

- Modify and utilize the transformation function in `transform.py` for processing raw data.

### 3. Storing Files on AWS S3

- Set up an S3 bucket (e.g., "spotify-etl-sn") to store raw and processed data.
- Adjust the S3 path in the Lambda function to store files properly.

### 4. Building Analytics Tables with AWS Glue and Athena

- Use `glue_script.py` as an AWS Glue job script to define and run ETL jobs.
- Execute the SQL script `analytics_tables.sql` in Athena to create analytics tables.

## Prerequisites

Ensure you have the following installed and configured:

- AWS CLI and AWS credentials.
- Python environment with necessary packages (boto3, requests, etc.).
- AWS Lambda, S3, Glue, and Athena services set up in your AWS account.

## References

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [AWS Glue Documentation](https://docs.aws.amazon.com/glue/)
- [Amazon Athena Documentation](https://docs.aws.amazon.com/athena/)
- [Spotify API Documentation](https://developer.spotify.com/documentation/web-api/)

Feel free to explore and adapt the code to fit your specific requirements.
