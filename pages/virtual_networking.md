# Virtual Networking

## Subnet

### Subnet security

1. NAT gateway
2. NSG (Network Security Group)
3. Route table

## Route Tables

### Network Virtual Appliance

It is simply a virtual machine with a preconfigured software installed. An image of this setup is usually called a virtual appliance.

Used to deploy packages for tools like Firewall, IDS, web filtering, DDoS protection, etc.

We must enable ip forwarding on the VM that will be used as an NVM (Network Virtual Appliance).
```diff
- What exactly is ip forwarding?
```

#### Creating virtual appliance test

Create normal vm, in it's NIC card, enable IP forwarding. Then run this to allow the windows vm to become a 
> router?

```bash
Set-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters -Name IpEnableRouter -Value 1
```

To enable pinging a vm, we must add this rule to a vm.
```bash
New-NetFirewallRule -DisplayName "Allow ICMPv4-In" -Protocol ICMPv4
```

```diff
+ Future, could setup proper virtual appliance 
+ software that monitors traffic
```


### Propagate Gateway routes 


### Route tables 

Route tables are used purely for outbound traffic. When there is no user defined route table, Azure automatically uses system routes that are defined by Azure. 

When we attach a route table to a subnet, then any outbound traffic from the subnet will go through the route table (the next hop).

A route configuration consists of a 1. destination ip addresses/CIDR range. If any outbound traffic matches it, 2. Decide next type of hop, and put 3. ip address to hop to.

> We have to enable IP forwarding on the *NIC*. Why is that?


## Azure DNS
> I could setup my own private DNS server and link my current DNS server as parent to my own private DNS

Try to create a DNS server within the vnet so we do not have to use the one provided by Azure.

### Azure DNS Zone

Instead of using name servers provided by domain companies, we can instead bring the configuration into the portal by using this service.


### Azure Private DNS Zone

