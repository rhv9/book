# SAS Keys and Azure AD

There are 3 ways to authenticate with Azure to gain access to storage services:

1. Access Keys
2. SAS Keys
3. Azure AD

We will first look at Access Keys and SAS Keys.

## Access Keys

Access keys basically give you full ownership over the storage account. It allows you to read, write, modify or delete any storage service in the storage account. A key that works for all. 

There are two keys: key1 and key2. The purpose of having two keys is to facilitate rotating of keys. It is good practice to rotate keys and when you rotate an access key, the older key is immediately invalidated. Thus, we can imagine production machines would temporarily be haulted until the new key is swapped in.

By having key2, we can now make all our production use key2 (which has the same freedom as key1) and then rotate the other key (key1). Then you could swap back to key1 or stay (on key2 and ping pong the current key being used)and repeat in a fixed period of time.

## SAS Keys

> It is actually two types but they all have different levels of access.

Shared Access Signature are keys you can generate that work for a period of time with restricted access to different levels of services. There are three different types of SAS tokens, each giving different granularity of access. It is important to note what they share in common:

1. All can specify period when key is valid.
2. All allows whitelisting IP addresses that can use the key.
3. All can enforce HTTPS or HTTP.
4. All can restrict actions the key is authorised to perform (read, write, delete, ...)

Now there are three types of SAS tokens:

1. Account SAS: it is a shared access key generated that can be used for more than one storage service (blob, queue, table, file share).
2. Service SAS: it is a shared access key generated for only one service. For Blob storage, you generate a SAS token to provide access to the container.
3. Object SAS: shared access key generated per object in any container. (eg. a blob file.).

### Pros

### Cons

### A problem with SAS Tokens

One major problem with SAS tokens is that once it is generated, you cannot deactivate that token. The only time it will deactivate is if has passed it's expiry date. Therefore, managing these tokens will be harder and pose a security risk.

A better solution is to use Access Policy.

## Access Policy

Access policy allows you to write stored service SAS tokens. Stored meaning you can view all the tokens. These differ from SAS tokens in that instead of embedding start and end time of token into the URI, it instead only has the start time and name of policy. The real benefit is being able to remove the access policy. This will invalidate the token, thus giving control in it's lifetime after it is generated.

> This does not support Account level SAS. Thus, a generated key will always be active for its time period.

```diff
- I am not actually sure if it has start time embedded into URI.
```


## Azure AD

The new way to authenticate is to use Azure Active Directory accounts. We can create groups and give individual account different levels of permission. There are two types of permission, we can give specific service level permissions (Blob, Queue,...), or storage account level permissions. 

Storage account permissions only allow us to manage the storage account (e.g access torage account portal). Without the actual data permissions, we cannot view the data.

Likewise, data permissions only give us access to the data, meaning we cannot acccess the storage account space with just this permission.
