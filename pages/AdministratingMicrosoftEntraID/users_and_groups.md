# Users and Groups

When you create a Tenant (Azure EntraID), we have to add users to it before they can use the services of Azure under that tenant. The user who created the tenant is automatically assigned as a Global Administrator role, and is Owner.

Users by default are granted *zero* permissions (Zero trust policy).

There are two types of users we can add to a Tenant:

1. Member

A member is a user we create directly inside a Tenant whose username will be under a *domain name* that is verified in the Tenant you are creating in. 

By default, all tenants get a verified domain name based on the identity of the creator. So if you created it with identity of ```johncena@outlook.com``` then the default domain name will be ```johncenaoutlook.onmicrosoft.com```. Then new users added under this domain name will look like ```fresh-grad@johncenaoutlook.onmicrosoft.com```

2. Guest

A guest user is a user who is invited by email. The invited user will then have to accept the invite. 

## Service Principals

Service principals are special identities created for applications to use when trying to authenticate to developed applciations. Its login credentials consist of a client ID and client secret.

## Groups

There are two types of groups:

1. Security Group

A group you create to give access to resources under a Tenant. Users can be actual users, devices, service principals and even other groups. You can also assign licenses.

You can setup licenses to automatically be assigned to users.

Group assignment can be manual or dynamic based on conditions according to the user's profile.

2. Microsoft 365 Group

These can have only users. Good for make collaboration easier between members of the group through shared drive, calendar.

### Group Assignment: Dynamic users

We can automatically add or remove users from a group using dynamic users list. 

Assignment is based on pre-defined rules based on the properities of the user. We can create a logical combination of properties to determine if a user is a member or not.

> Note: Once you have used Group Assignment, the option to manually add members is gone.
