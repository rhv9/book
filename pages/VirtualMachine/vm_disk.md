# Virtual Machine Disks

- unmanaged disks have max of 20,000 IOPS in storage account.

> When creating disks, we have to consider the IOPS of disk AND the VM's max supported IOPS. 

- Most VMs now support premium storage, however, there are still select few VMs that can only run on standard disks.


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
