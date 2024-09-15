# Introduction Azure Monitoring and log Analytics 

Azure Monitoring is a centralized service provided by Microsoft that collects metrics and activity logs from applications, operating systems, azure resources, azure subscription and azure tenant and allows you to process the data in various forms.

Why is monitoring important? When you have applications that are running, we need to know how it is functioning, if it is functioning and other data for debugging purposes. These telemetry allow us to quickly respond to criticial issues, ensuring high availability of services and applications.

Alerts

## Types of data

1. Metrics - This is data about performance, health and availability of resources. This includes cpu usage, memory usage, ingress and egress of network data, IOPs, etc.
2. Activity Logs - These are data that has to do about any activity of a service. These include creation of resources, modifying properties, and by whom these actions were taken. Audit logs basically.
2. Logs - These are any data that is generated overall, including activity logs. These can include diagnostic data, logs creating by operating systems (syslogs or Windows Perf Counter).

## Costs

- Azure portal logs are free. These are automatic, default activity logs and metric data that are collected by Azure resources.
- Using API to access logs there is a cost.
- If storing logs, it uses Azure Storage service which has its own costs.
    - These can be archived for 

## What you can do with the data

- Visualize metric data against time to analyse and get insight into the services.
- Gather audit logs to see how resources and services are modified.
- Cost analysis based on metric data.
- Setup alerts if a certain metric usage has been reached
