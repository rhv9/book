# Azure Private Endpoint

Azure Private Link enables to you to access Azure PaaS servuices like Azure Storage, SQL Database over a private endpoint in your virtual network.

cross-tenant

## Private endpoint service

To use private endpoint service, the following conditions must be met:

1. VNet and Microsoft PaaS must be in same region. VNet and storage account in EastUS region.
2. Both must be in same subscription?
3. Both must be in same resource group?
4. Both must be under same Azure AD tenant.

```diff
- What are Application Security Groups?
```

Ensure that the endpoint DNS is handled. One option is to use private DNS Zone. If you have your own DNS server, configure to support it. Or add it to host files in virtual machines.

> If the services were in different Azure AD tenants, then the steps would be different and likely require handshake from both ends.


> Setting all this up does not mean that the public endpoint is now blocked. No. It is still accessible. To block it, go to Networking and disable public network access. That setting has to do with the public endpoint.