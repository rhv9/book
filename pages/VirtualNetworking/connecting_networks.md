# Connecting networks

A virtual network in the cloud is completely isolated. This means a VM in one vnet cannot communicate or even know about any other VMs in other vnets. 

There are multiple reasons to connect vnets:
1. Point-to-Site: we want to access resources from our local network. Basically, you can access a VM in cloud vnet from your local machine with a private address.
2. Site-to-Site: Sharing resources, database only on premise that needs to be used by cloud site.
3. VNet-to-VNet: A vnet in one region need's to communicate to vnets in another region.


There are three different ways to connect
1. Point-to-site VPNs: configure individual on-premise computers. No extra hardware, only complete configuration process.
2. VNet-to-VNet: VNet peering, no additional costs.
obsolete option was VPN gateway setup on both VNets and connect them.
3. Site-to-Site: Hybrid cloud. Additional hardware needed. Need to configure a VPN device.

### Express routes
Instead of using VPNs, we can use express route to directly route all traffic via a dedicated line straight to Microsoft infrastructure. VPNs work by creating encrypted tunnels to Microsoft Infrastructure via the internet. 


## Point-to-Site VPN

A VPN tunnel needs to be established to allow local computers to connect to cloud VNet.

Need to create a VPN gateway and a server certificate and client/s certificates.

```diff
- What is a certificate server installed on enterprise
```

Since do not have certificate server, use self-signed certificate.

## Some key points regarding setting up

```diff
- He said he will discuss active active mode.
- What is GPG (Border Gateway Protocol)? He said it is about using route tables to divert traffic from vnet to on-premise.
```

- Point-to-site configuration: Give an address pool to give private ip to computers that connect.
- Tunnel type???
- Authentication types??? Azure certificate vs RADIUS authentication, Azure Active Directory.

To prove it is working, we can use NetworkWatcher or RDP, or starting web server locally and being able to access it from VM inside VNet.

## VNet Peering

The new method of connecting vnets in cloud instead of VPN Gateway. Seamlessly connect two vnets.

**Benefits**
1. Easy to setup
2. Works cross region
3. All traffic is private and routed through Microsoft Infrastructure.
4. Deploy over subscription and regions.

**Cons**
1. Peering is not transitive. Therefore, if VNet 1 peered to VNet 2 and VNet 2 peered to VNet 3, VNet 1 cannot communicate to VNet 3.
2. No overlapping IP address space or range?

The VNet peering page will create vnet for both this and remove vnet.

Vnet syncing is required when editing any of the vnets address space.

### Configuration

There are 4 main configuration settings when creating a vnet peering to control what type of traffic is allowed.

From the local perspective:

1. Traffic from local to remote vnet is allowed.
2. Forwarded traffic coming from remote vnet is allowed into local vnet.
3. Allow gateway or route server traffic from local forward to remote vnet.
4. Gateway or Route server traffic forwarded from remote is allowed to local vnet.

### VPN Gataway

We can use VPN Gateway to configure P2S VPN. 
