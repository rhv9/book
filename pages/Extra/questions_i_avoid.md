# Questions I avoid

## VM

1. What about availability sets?
2. How much CPU and RAM?
3. How much space?
4. How to create credentials using Key Vault
5. How to use config-init for Ubuntu server.
6. How to use extensions.
7. How to use same ssh key pair for multiple Linux VMs.
8. [Availability zones](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview?tabs=azure-cli) vs [Availability sets](https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview).
9. Fault domains and update domains. What is a fault domain?
10. How to keep your VMs as fault tolerant as possible. 
11. What are the possible errors that could cause downtime for VMs?: Operating System, Application, Rack failure, hardware maintainance, datacenter failure, region failure, availability zone failure.
12. Azure Spot Instance? What may cause eviction?

### To know

1. Windows VM support [hot removal](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/detach-disk) of data disks.

## Virtual Network

1. What is an IP Group and what can you do with it? (An IP group is a user-defined collection of static IP addresses, ranges, and subnets.)
2. What are the limitations of a NIC on a VM? What is the extent of what you can achieve with it? (A network interface is used to connect a VM to a subnet - Microsoft Learn 2024.)
3. What is a network bridge in Windows Server?

## Storage

1. What is Azure Data Lake Storage and limitations of it.
2. What parameters are added for each SAS Tokens.
3. How to ensure data is [immutable](https://learn.microsoft.com/en-us/azure/storage/blobs/immutable-storage-overview?tabs=azure-portal)? 

## Entra ID

1. How to add custom domain to tenants, services, etc.

## Azure Governance

1. What are the different ways I can use remediation action? What if it is a property that cannot be changed without recreating resource? What if there are multiple allowed values, do we set which value for any that do not meet?q

## App Service Plan

1. Can you create Windows and Linux app service plan in the same region and same resource group? What combination is not allowed because in the past, there were restrictions.

## Not as important


1. What is OAuth and OpenID Connect?