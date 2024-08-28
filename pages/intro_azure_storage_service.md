# Azure Storage Service

## Introduction

Where the data will be stored.

Three types of data:
1. Structured data: Tables, database, relational database, SQL
2. Unstructured data: Binary data
3. Partially structured data: JSON, XML, CSV

There are three important factors when dealing with storage, you want them to be **scalable**, **durable**, and **highly available**. These three is what Azure provides.

1. Scalable: Start from few KBs up to TBs of data
2. Durable: Replication of data
> What are the options?
3. High availablity: Availability zones and region copy.
4. High security: Data is encrypted at rest.
> Is this for all data, or can you choose?
Charged only for what is used!

## Types of storage services

There are 4 main types of storage services offered:

1. Blob Storage: Can store anything, any data file. Binary Large Object. Sometimes referred to *Object Storage*. There is no directory structure, only one container holds everything. Can use paths to create "hierarchy". It is about 3-4 times cheaper than blob storage.
2. File Storage: Similar to Blob storage, except provides directory hierarchy for organising files. Good for legacy solutions where we want older systems that use file system to work straight into cloud. Otherwise, the modern and better solution is to use Blob Storage. 
3. Table Storage: Stores partially structured data. NoSQL key-attribute. Cheap compared to CosmosDB. Good for initial testing and starting out, but preferred to move to CosmosDB.
4. Queue Storage: provides messaging for communication between components of cloud services.