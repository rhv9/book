# Azure Backup and Restore

Azure provides a service for backing up any VMs, either on Azure cloud or on-premise, 

## Benefits of Azure Backup

- Unlimited Storage
- Incremental Block-level backup: Save storage by only storing what has changed.
- Unlimited ingress and egress traffic.
- No upfront infrastructure cost, only pay as much as you use.
- Storage options for high availability
    - LRS data replication
    - GRS data replication
- Can take application aware snapshots

## Types of backups

### Crash-consistent Backup
- This is a snapshot of the data on the disk. It does nothing to ensure application data is stored.
### Application Aware Backup
- ???

## Backups

### Azure IaaS VM Backup using Recovery Service Agent

- Only backup Azure VMs
- Recovery Service Agent is automatically installed when doing first backup
- Can only backup Azure VM and data disks (only crash-consistent backup)
- Supports both Windows and Linux

### Microsoft Azure Backup Service (MABS)

- Backup both azure and on-premise
- Can do Application aware backup
- Stores files, folders, applications, VMs, data disks.

## SC-DPM
