# Python Uploader
This repository is used to upload files from temporary space to SharePoint portal through AWS Lambda

## Pre requisites

1. AWS VPC
2. AWS InternetGateway, NatGateway
3. AWS Public & Private Subnets
4. AWS Lambda & Layer
5. AWS S3 Bucket [optional]
6. AWS Cloud watch event[optional]
7. Python 3.8.2

## How to use ?

* Configure AWS VPC
* Create Public & Private Subnets and associate to above VPC
* Create & Configure Internet gateway and associate to Public Subnets
* Create & Configure Nat gateway and associate to Private Subnets
* Define the route tables
* Create a lambda function and associate to above network to upload files
* Create a lambda layers with required modules
* Load the script and set environment variables
* Ensure your Lambda has access to all the resources which requires.
