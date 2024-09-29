# Load Balancer

It is a layer 4 (TCP/UDP) load balancer that distributes incoming network traffic across healthy services instances in virtual machines defined in a load-balanced set.

The purpose of a load balancer is to ensure high availability and scalability by enabling you to scale instances of your service in the backend of a load balancer.

It uses a hash-based distribution algorithm that uses the 5 tuple of a transport layer packet to map traffic to available servers.

- provides stickiness of clients. It ensures for the duration of a transport session (TCP or UDP), all of a clients traffic goes to the same instance so that any state generated in server instance is accessible to user.

## Types

- SKU type: 
- Tier: Regional or Global
    - Global is only supported for Standard SKU
### SKU

> Basic SKU is deprecated and so is Public IP address services by Sep 2025.

Basic is free. Basic only supports availability sets or VM scale sets. Cannot add individual VMs. Standard support any combination. Basic also does not support outbound rules (SNAT).

### Standard SKU

- Standard SKU type requires a Standard Public Ip address if you want public access
- Up to 1000 VMs
- ingress and egress traffic cost and cost per rule.

### Gateway SKU

This is a more advanced SKU that is needed for more niche purposes. Typically standard is sufficient, and if you need some of the features of Gataway, there are better alternatives. 

- Can seamlessly add NVA such as firewall to route traffic from load balancer to firewall, and then to VMs

## Features

1. One of the features of Load Balancer is that it can do NAT. So you can map port number to specific instances. In Azure Portal, you find this under Inbound NAT rules.

An demo could be to RDP into a VM behind a load balancer. But the VM does not have a public ip address. So then we can add an inbound NAT rule that specifies any traffic on port 3891 (can be any) maps to virtual machine 1.


## Limitations

- All VMs must be from the same VNet.

### Creating

## Load balancing rules

Add rule to configure load balancing. Here you select the frontend ip, then select what source port should map to destination port in backend pool

You also create a *health probe* checker and configure interval of checks and number of consecutive fails before it is marked unhealthy.



[*Session persistence*](https://learn.microsoft.com/en-us/azure/load-balancer/distribution-mode-concepts) can be either client IP, or both client IP and port, or None. It is strongly recommended to use None to ensure even distribution of traffic and best utilisation of all instances. 

- To use None, ensure that the service instances are stateless e.g adopting REST API design.

For None, session stickiness is only guaranteed.

> Why is other options than None bad?

**Idle timeout** for TCP connections when client does not send keep-alive packets. Default is 4 minutes and can go up to 30 minutes.

