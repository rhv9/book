# Entra ID Tenants

Tenants/Directories - this is an isolated instance of Entra ID that manages users and groups within this instance. Typically one organisation has one tenant which will contain all of its users.

## Types of Users

1. **Create a user**

Create a user account and share login credentials.

2. **Invite a guest user**

Send an email invitiation to a user who has its own Identity Provider.

## Types of Entra ID instances

1. **Entra ID** (formerly known as Azure Active Directory)

This is Entra ID where each user within the Entra ID must be created by an administrator account and then the user will be given the login credentials to login, change their initial password and access/perform tasks within the scope of their role.

This form is most similar to Microsoft Active Directory, where each user is created by an admin.

2. **Azure AD B2C** (Azure Active Directory Business to Consumer)

This is a public Entra ID where users are able to register a user account on Entra ID on a self-service basis. Users register an account with an Identity Provider of their choice (eg. Google, Facebook, Amazon).

We can govern the roles users have, and what the users are authorised to perform and access. This is typically used when we want to give access to an application to the public.