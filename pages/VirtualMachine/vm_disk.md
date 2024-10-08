# Virtual Machine Disks

There are three disks involved when using a Virtual Machine:

1. OS disk: This is where the image OS is stored. Gen 1 up to 2TB. Gen 2 > 2TB.
2. Temporary Disk: This is a non-persistent storage disk local to the VM. Good for high performance caching of files eg pagefile.sys.
3. Data disks: This are other disks we can attach to a VM.

OS and data disks are page blob storage in storage account.

**Data disk**

Data disks have a maximum of 32TB. We can do whatever we want with this, create partitions. 

> One thing to note is if an image has a data disk, then when using the image to create a VM, it will create and attach the data disk as well.

> Note: During the olden Azure days, the max data disk size was 1TB. So we had to use virtual disk service called Storage Space to create a large disk comprised of several 1TB data disks.

## Types of disks

**Unmanaged Disk** - we manage a storage account storing a .vhd page blob storage. It is not recommended to use unmanaged disk (unless need access to .vhd file) as there will be additional management when scaling due to max 20,000 max IOPS of a storage account.

**Managed Disk** - Azure manages the storage acccount so you will not have to worry about scalability. Only need to specify size of disk and performance tier (standard or premium).

- unmanaged disks have max of 20,000 IOPS in storage account.

- Most VMs now support premium storage, however, there are still select few VMs that can only run on standard disks.


## Managed Disks

Read in detail at [Microsoft's documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types).

Azure currently offers five disk types:

1. Standard HDD
2. Standard SSD
3. Premium SSD
4. Premium SSD v2
5. Ultra Disk


## Converting from Standard to Premium

Unmanaged: Create a Premium disk and copy all data from .vhd file of standard disk.

Managed: Can change to premium from configuration.

> Note: When changing performance tiers and sizes, the max IOPS and THROUGHPUT depends on both the DISK and VM. Disk may have high throughput, but if the VM does not support it, it will be a waste.

## VM Disk encryption

Can use microsoft managed keys or customer managed keys (key vault).

Windows uses bitlocker, Linux uses DM-crypt.

Look at the table in the document.

## Disk snapshots

Capture a snapshot of disk at a particular point of time. We can use this snapshot for any disk.

Initial snapshot of disk will be a full snapshot. Every subsequent snapshots on the disk will be incremental. 

The advantage is that you can create a disk with the snapshot.

## Capture image VMs

1. Generalized image: is the copy of the live machine
2. Specialized image: 

## Virtual machine scale sets
