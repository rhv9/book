# How are Azure Subscriptions and Azure AD related

1. Need to create Microsoft account using any email service.

Now what is the relationship between Azure Subscription and Azure Active Directory.

## Azure Active Directory

It contains Users, Groups and Service principles.

Service principles (App registries page) is an identity that an application can use to have an identity to communicate with Azure resources.

Account Administrator is the account who is responsible for a subscription and Azure usage is reported. This includes tasks like handling billing.

The domain name is by default created based on the account admin that created it.

**Subscriptions are a container for billing**

One subscription has one account administrator but one adminstrator account can have multiple subscriptions.

Azure Active Directory has two types of users:

1. Members - You create a user and you can create profile for it.
2. Guests - This is an invitation to join the AD by email.

Think of AD as different organisations.

- Whenever a user logs in to portal.azure.com, it has to select one AD Tenant. Once I switch to a particular AD, I can only view the subscriptions of that AD.

> Every member and guest added by default have no permissions on AD and Subscriptions. Therefore in the start, they cannot see any subscriptions.

### External Identities
You can select external identity providers. By default, it is Microsoft Entra ID, Email one-time passcode, and Microsoft. You can also add Google and Facebook.