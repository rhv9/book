# Creating Storage account

This page will document some important points to consider when creating storage account.

## Performance

1. Standard: All services will run on a HDD. Lowest cost/GB. Slower IOs. Best for storing large amounts of data not frequently accessed and/or in large amounts, where latency and speed is not a priority.

    Also supports all types of storage accounts.

2. Premium: All services will be run on a SSD. Very fast IO operations and latency but more costly/GB. 

    Queue Storage not supported.

> What cases will standard performance be sufficient and what purposes do we really need premium?

## Redundancy

1. Locally-redundant storage (LRS): 
2. Zone-redundant storage (ZRS):
3. Geo-redundant storage (GRS):
4. Read-access Geo-zone-redundant storage (RA-GZRS):
5. Geo-zone-redundant storage (GZRS):

The table below highlights main points. It is ordered based from lowest cost to highest cost. Also ordering applies to availablity.

Note: copies within single datacenter (storage unit) are spread across Update Domains and Fault Domains to ensure highest availability.

- P = Premium support
- C = Number of copies of a write operation.

The table is ordered in increasing cost and availability statistic.

| Type | C | P| Description |  
|-|-|-|-|
| LRS | 3 | Y | Replicates data only within single datacenter in that region. |
|||| Write operation is successful after all 3 copies are made. |
| ZRS | 3 | N | Replicates data across 2 or 3 availability zones. Good for strong consistency, durability and high availability|
|||| Write operation is successful after all 3 copies are made? |
|||| In the event of a zone outage, data can still be R/W from other zones. |
|||| Good also if your data must remain within region due to laws and regulations. |
| GRS | 6 | N | Replicates data in one datacenter in primary region and one in secondary region. |
|||| Replication is asynchronous to secondary region. So it is successful as soon as it has written to primary region. Thus latency of write operation is against primary region.  |
|||| Automatic failover to secondary region. |
| RA-GRS | 6 | N | An option of GRS where secondary region can be used for reading. |
|||| Access keys work for both primary region and secondary region url. |

- **transient fault handling** is about when a zone goes down, automatically handling switching to using other zone seamlessly. It is important to implement retry policies with exponentional-back off << I don't understand this part>>
- Geo redundancy has the concept of primary and secondary region.
- Replication within a region is done synchronously, meaning one write after another.

## Advanced

- HTTPS only
> Look into the limitations of enabling HTTPS, as there are issues.
- Access data either key access or AD account
```diff
- Data Lake Storage Gen2?
```
- cross-tenant replication


## Costs

1. Storage costs
2. Data access costs
3. Transaction costs
4. Geo-replication data transfer costs
5. Outbound data transfer costs
6. Changing the storage tier - Cool to hot incurs read charge on all existing data. Hot to cool incurs write charge on cool tier.

## Data protection

```diff
- Need to check.
```
