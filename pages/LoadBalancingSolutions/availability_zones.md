# Availability Zones

Availability zones are isolated datacenters within a given region. They have their own cooling, power supply and building that are physically separate from other availability zones within the same region.

Availability zones is a solution to ensure high availability of applications such as distributing load across regions, creating redundant resources in other zones, or using zone-redundancy services.

One option is you can select the zone in which you want to create a resource like VMs. We can then manually spin up VMs across multiple availability zones to ensure that if there is an *outage* of one of the zones, then the clients can still use resources in the other availability zone.

There are other services that offer zone-redundancy services such as Storage account. It provides a platform for automatic duplication of data across multiple availability zones.

Also important if you want to ensure high availability and are **bound by compliance constraints** of requiring data to be within a region.

## Cost

What has costs:

- There is ingress and egress cost associated with network traffic between availability zones.

What does not cost:

- No cost in network traffic within same availability zones