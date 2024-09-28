# Availability Sets

Planned maintainance

Unplanned maintainance

Update Domains and Fault Domains, logical vs physical

Performance group/close together

Limits of Availability Sets
1. Generally recommended to have same size. If changing size, it if does not fit, then all machines need to be stopped and moved to another hardware cluster
2. 200 VMs in one availiability set
3. Scope is limited to one region. It does not span across regions
4. VM availability set must be set at creation of VM.
> Is the scope limited to regions or zones?

## Best Practices

1. Ensure they are the same size
2. Do not mix application tiers such as web app and database in same availability set.
3. Use load balancer

