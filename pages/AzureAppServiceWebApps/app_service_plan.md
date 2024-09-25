# App Service Plan

App Service plan is a service that manages the Infrastructure (VM/s) for you to deploy app services on. You can think of the layers like: App Service > App Service Plan > VMs > Azure Hardware. 

Multiple app services can be deployed on the same app service plan.

An app service plan is defined by:

1. Location
2. SKU = The type of VM hardware. The list includes Free, Shared, Basic, Standard, Premium, Isolated. The SKU determines the features that are available e.g. Deployment Slots
3. Instance Size = This determines the power of the SKU. If you use Basic SKU, then instance sizes are Basic B1, Basic B2, and Basic B3, increasing in processor and memory with the number.
4. Scale count = This determines how many of the same VM is running. Literal duplication. 1 VM, 2 VM, etc.
5. OS: Windows or Linux

## Features

- Infrastructure: Shared, Dedicated and Isolated.
- Number of Deployment Slots: 0, 5, 20,...
- Number of vCPUs.
- Size of RAM.
- OS: Windows or Linux.
- Manual Scaling or Auto Scaling or No Scaling.

## Things to consider 

Multiple app services can be deployed on the same app service plan. This means that each app service is running on the same hardware, sharing vCPU and memory.

Some things to consider when deciding to isolate app service or share the same app service plan:

1. Different scaling requirements: If app service plan scales, then each app service gets scaled which may a waste of resource.
2. Different OS. 
3. Sharing of memory and processing units.
4. Location.

## Moving

You can move an app service to another app service plan if it is in the same region. Before, it was a requirement for the app service plans to be in the same resource group and region, but now that requirement is voided.

If you want to move the app service to an app service plan in another region, you could clone the app service to another region and then delete this one. But you cannot move directly.