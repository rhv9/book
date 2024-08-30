# Blob Storage

Within Azure storage account, all blobs are added under a container. First, make a container to put the blobs into

**Container access level**
1. Private
2. Blobs only
3. Container and Blobs

The url of a file is in the format blow. This can be appended with parameters for other blob features or adding access key.
```
https://<storage account name>.blob.core.windows.net/path/to/file
```

Individual blobs can be set to use hot or cold access level.

You can upload files into the container directly from Azure portal. For more efficient management, use AzCopy tool.

## Types of Blobs

Choosing the right type of blob is important in managing number write operations and improving read/write times. 

#### Block sizes
A file being broken down to multiple blocks means that parallel downloading and uploading of files is possible, improving upload and download speeds. 

```diff
- Update block blob by reading docs. Outdated.
```

| Type | Block size | Best for |
|-|-|-|
| Block blob | Up to 100mb | Best for storing files to be read or overwritten to. |
| Append blob | Up to 4mb | Appending to file e.g logs. Only operation is to append to the file. Does not expose blockid.|
| Page blob | 512 bytes | Optimised for random R/W. Decide max size of page blob. Pages are accessed/updated based on an offset. Disks for VMs / .vhd|

- Note: Page blob and block blob both have a maximum of 50,000 blocks per blob. Therefore, block sizes will affect the maximum size a blob file can be.


## Blob features

Appended to url.

### Snapshots
Can save a particular state of file as a snapshot which you can access by appending snapshot parameter to url.

### Versions
A record is kept of the different versions of a blob when it is changed. Read more specifics on docs.

### Lease
Leasing a blob adds a lock to a blob file, making it unmodifiable or delete without using a lease key that is given when leasing.

## Metadata and item tags

A blob file has a bunch of metadata, like last modified, if it is archived and the rehydration status, etc. These are key-value pairs of data about the blob file. 

Item tags, similar to metadata, are also key-value pair data that can be attached to a blob file. The difference is that item tags are indexable for Azure Search. Another difference is that modifying a tag will not affect the last modified date in metadata.

## Lifecycle Management
A set of policies/rules can be applied to blob files to change its access tier and if it should be deleted by time since last modified.

We can add a chain of conditions so that a blob file goes from hot to cold after 30 days, after 180 days it will be archived, and finally after 365 days it should be deleted.

These rules can be applied to whole containers or filters can be added to better select certain files.

## SAS and Access keys

Access key is a key that gives full access to a storage account. Full R/W and view of data that is also private. This will become the legacy option in favour of Azure AD authentication. More on that in the next section

SAS keys can be generated per blob file to make them accessible for a period of time. These will then expire.

### Access key best practices

Keys should be rotated in a timely basis for security reasons. However, we do not want production machines to have downtime during the time the key is rotated and updated to apps.

As such, it is recommended to have two keys. The first key is used in production. When rotating first key, we can make all apps use the second key, which will also work and cause no app crashes. After the first key is rotated, apps can then make use of the first key again.

## IAM

Azure is slowly transitioning over to authenticating most services via Azure AD account.

There are two permissions necessary to have same access level as Access keys. One is Storage Acount Contributor to get full access to the storage account, giving you permission to use the it on Azure portal. The other is Blob Container Contributor which will give you full access to view, modify and delete blob files in the container.

## Azurite / Azure Storage Emulator
> Note: Azure Storage Emulator is deprecated and is now the open source, cross-platform Azurite.

Azurite is a tool that allows you to spin up a local Azure storage account for development/testing purposes

