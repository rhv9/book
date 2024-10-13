# VM Backup and Restore - Recovery Service Vault

This section covers how to backup and restore Azure VMs using the Recovery Service Vault.

This service also works for private Azure cloud (Azure Stack), Azure SQL VM, and on-premise systems.

## Recovery Service Vault

Recovery Service Vault is a service that is built into VM Service that allows you to easily configure timely backups and seamlessly restore snapshots created.

These snapshots are called Restore Points. Restore points are snapshots that are kept locally to the VM disk to allow fast recovery of disk. 

You can have up to 500 Recovery Service Vault in a single Subscription. But that does not mean each VM must have its own Separate vault, you can backup several VMs on a single Recovery Service Vault.

> NOTE: The Recovery Service Vault must be in the same region as the VM.

***Encryption***: SSE Encryption applys to the saved snapshots (encrypted at rest). If using ADE, the keys from Key Vault will also be backed up.

To get started, create a Recovery Service Vault. Then go under getting started to find the Backup tab.

#### Backup

When creating a backup, we will select to backup an Azure VM. Then we will have to create a backup Policy

**Backup Policy** allows us to create a plan for the backup. Here we can decide the frequency of backups, How long a quick restore point should last for daily, weekly, monthly and yearly and the retention periods for each restore point.

Once we create it, it will then follow the schedule to backup the VM.

After the first backup, the VM will installed the necessary agents, listing *VMSnapshots* under extensions tab.

## Viewing backups: Backup Jobs

Use backup jobs to view the backups created. We can see the success status. We can also see the VMs that are being backed up under this service and select one to see all the restore points. In this page, we can also manually backup.

## Restoring

View a snapshot and then you can click three dots and do restore. We have the option to create a new VM instance or replace the disks for the current VM. Ensure VM is shutdown before replacing.

We can also do File Recovery where we mount the disk and recover any files we may want. On the learning material, it worked when inside an Azure VM. Although it should also work locally.


## On Premise Backup and Restore: Files and Folders

Select Backup and on-premise. Then it will provide the necessary backup service agents to install on the machine that will be backed up.

Backup:
- After installing, we have to do some setup. 
- We can save specific files and folders with exclusion filters.
- You will have to create a passphrase for encryption and a place to store a copy of the passphrase to ensure you do not lose it.
- Then backup.

Restoring:
- Same story, ensure agent is installed.
- Do recovery.
- You will then select the service vault and use passphrase to access
```diff
- the procedure is not fully correct.
```
- Mount the volume and you can copy and paste the files and folders.

## Deleting Resource Servicee Vault

To delete, ensure Backup Infrastructure and Backup items are empty. After doing so, you will be allowed to delete the vault.
