# Disk Encryption

Below are the following ways data disks are and can be encrypted for Virtual Machines. These are to ensure higher levels of security and compliance with high security standards like HIPAA.

## Software Service Encryption

This is a default service provided by Azure. It is encryption at the hardware level for all storage accounts in Azure. All storage account disks are encrypted at rest. When reading, data is automatically decrypted and when stored, data is encrypted. 

There is no noticeable penalty in IO performance for VM as decryption happens at the storage hardware, not by the VM vCPU.

- Default, platform managed encryption uses 256-bit AES encryption.
- **This service cannot be disabled.**

To use Customer Managed Key for encryption:

1. Create a Key Vault and ensure purge protection is enabled.
2. Add an encryption key to the key vault.
3. Create a Disk Encryption Set and add the key to key vault.
4. Give get key permission and wrap and unwrap cryptography permissions to disk encryption set under vault access policy for key vault.
5. Now under the disk, select the disk encryption set created in the previous steps.

## Azure Disk Encryption.

This is an option you can select for VMs to encrypt disks at the Guest OS level. It uses BitLocker for Windows and DM-Crypt for Linux. Not only will there be SSE encryption at rest, but the data when transferred from Storage to Compute will also be encrypted and need to be decrypted by the OS during runtime for all IOPS.

This will have a small but negligible performance impact on the CPU as the processor will have to decrypt data in storage. If you are running very intensive CPU tasks, then ADE will have a more noticeable impact. An alternative and more balanced solution will be to only have the data disk with ADE and keep all data encrypted, whereas OS disk remains unencrypted.

> Note: The disk must use platform managed encryption.

To enable:

(Ensure key vault and disk encryption set (<-- I think?) are created.)
1. Go to disk under the VM and go to additional settings.
2. Under encryption, select OS or OS and data disks.
3. Now we will notice under extensions for VM, there is a new Azure Encryption extension installed.
4. And we will also notice under disk, that it is encrypted with "SSE with PMK and ADE"

To disable:

1. RDP into VM
2. Remove extension from Azure Portal.
3. Turn off BitLocker for Windows, DM-Crypt for Linux.