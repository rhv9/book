# Creating Virtual Machine

> Check this link for creating with custom init. https://cloudinit.readthedocs.io/en/latest/reference/examples.html

Some of the main points to think about when creating a virtual machine can be broken down to these domains:

1. hardwareProfile
2. osProfile
3. storageProfile
4. networkProfile

## New points that are not in old video

- Hibernation
- Availability set preview to auto select. For each zone, a VM will be created. So 3 zones means 3 VMs.


## Disks

- Generally always use managed disks. Unmanaged disk means you get a storage account with a container containing a .vhd file.
- Each disk is LRS. The disk is locally stored.

## Networking

- Can create virtual network quickly from here or select one.
- Basic IP is not good for production. 
    - We can choose the routing preference, Microsoft network vs internet. First go to closest microsoft datacenter and from there travel to the datacenter or via internet.
- Quick page to create NIC NSG with ports to enabled.
- Accelerated networking

- Load balancing.

```diff
- Basic Public IP is deprecated and will lose support by September 2025.
```

## Management

- Basic Azure security centre
    - boot diagnostics
    - Enable OS guest diagnostics. You need to provide a storage account for this feature.
- Identity: System assigned managed id means ??
- login with Azure AD
- Auto-shutdown
    - if you know you will not need it at certain periods, set up auto shutdown.
- Enable backup
- disaster recovery

## Advanced

- Extensions??
- Custom data
    - Provide scripts, configs while it is being provisioned.
- Custom user data
    - pass scripts, config files or other data that the application will use during its whole lifetime.
> Note, custom data and user data does not provide a process to use this data. The image itself must be configured to use such data.
> Look at internet to find out use cases of custom user data and data to understand and find scripts to achieve some goal. For example for Linux VMs, we can provide a cloud init script to install apache2 web server and start the service.

### Azure dedicated hosts

Reserve hardware isolated at the physical level specifically for your purposes. You can take a batch of 64 virtual CPUs that you can use to deploy your Vms on.

### VM Generation

> Deprecated. All new virtual machines are now Gen 2 VMs.

Select Gen 1 or Gen 2 VM.



