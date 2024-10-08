# Creating Virtual Machine

> Check this link for creating with custom init. https://cloudinit.readthedocs.io/en/latest/reference/examples.html

Some of the main points to think about when creating a virtual machine can be broken down to these domains:

1. hardwareProfile: power
2. osProfile
3. storageProfile
    - OS
    - Data
    - Backup
4. networkProfile
5. location
6. pricingModel


## New points that are not in old video

- Hibernation
- Availability set preview to auto select. For each zone, a VM will be created. So 3 zones means 3 VMs.

## Instance details

- Availability options
    - Availability set: Multiple VMs in same zone/datacenter
    - Availability zone: Spread across multiple zones within a region
    - Virtual Machine Scale Set (VMSS)
- Image
    - Microsoft provided
    - Marketplace
    - Own images
- Azure Spot Instance: Using unused Azure infrastructure reserves at a cheaper cost but will be evicted when needed for normal workloads.
    - Two eviction options
        - Capacity only: Max cost/hr rate is set to normal Pay-as-you-Go workloads and if capacity is needed by Azure normal workloads.
        - Price or capacity: You set a max cost/hr rate you want and if instance will be charged more, it is evicted. If capacity is needed, then instance is evicted. (It is like bidding for the instance)
- Licensing: Up to 49% off if you have Azure Hybrid Benefit. Use on-prem Windows Server License to save on cost.


## Disks

- Types of disk: Premium SSD, Standard SSD or Standard HDD.
- Encryption: Platform managed keys, or customer managed keys or double encryption with both. All data is encrypted at rest.

- Advanced options:
    - Generally always use managed disks. Unmanaged disk means you get a storage account with a container containing a .vhd file.
        - Another point to consider is that a storage account has a max IOPS of 20,000 so storing disk of lots of VMs can reach this limit. (Will become a management issue)
    - Ephemeral disk: have your OS disk be created locally to the VM for better performance than remote Azure storage. Depends on size of VM.

- Each disk is LRS. The disk is locally stored on a datacenter.

- Can add data disks with lots of options. Read more at the disk section.

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

- Monitoring
    - Boot diagnostics: Store data on managed disk or own.
        - We can see a screenshot of loaded VM or BSOD screen and the serial logs of booting.
    - Enable OS guest diagnostics. You need to provide a storage account for this feature.
- Identity: System assigned managed identity is giving an identity from Azure Entra ID.
- login with Azure AD
- Auto-shutdown
    - if you know you will not need it at certain periods, set up auto shutdown.
- Enable backup
- Enable Disaster Recovery
- Guest OS Updates:
    - Windows automatic update: If you are okay with some downtime during workloads
    - Azure orchestrated update: across availability sets to ensure high availability.
    - Manual update.

## Advanced

- Extensions?? - Software and configuration installed after VM creation.
- Custom data
    - Pass scripts, config files or other data  **while it is being provisioned**. This cannot be changed once instance is created (I think). The file is stored as a ```.bin``` file in a specified path depending on OS. (This is the older option and user data is now preferred)
- Custom user data
    - Pass scripts, config files or other data the **application will use during its whole lifetime**. Same as custom data except you can get the data with a REST call so you can always edit it after.
> Note, custom data and user data does not provide a process to use this data. The image itself must be configured to use such data.
> Look at internet to find out use cases of custom user data and data to understand and find scripts to achieve some goal. For example for Linux VMs, we can provide a cloud init script to install apache2 web server and start the service.

### Azure dedicated Hosts

Reserve hardware isolated at the physical server level specifically for your purposes. You can take a batch of 64 virtual CPUs that you can use to deploy your Vms on.

For this you will need to create a Host Group service which specifies name, region and availability zone and fault domains. Then you create a dedicated Host on the Host Group which the VM will run on.

Good for:
- Ensuring higher levels of security.
- Controlling when the hardware will have its maintainance.

### VM Generation

> Deprecated. All new virtual machines are now Gen 2 VMs.

Select Gen 1 or Gen 2 VM.

> Look into what features are included with Gen 2. Some include UEFI-based booting, larger memory and cpu, vPMEM, SGX



