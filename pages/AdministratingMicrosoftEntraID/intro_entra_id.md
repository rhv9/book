# Introduction to Entra ID

[Difference between Azure roles and Entra ID roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/rbac-and-directory-admin-roles)



It is a solution for authenticating users, and authorizating to perform their required tasks.

> It was called Azure Active Directory and is now rebranded to Entra ID

## Uses for Entra ID

1. IAM solution - Identity and Access Management Solution
2. Provides SSO (Single Sign-On) access to all Microsoft applications (Office 365, OneDrive, Outlook, etc...)
3. Supports MFA Authentication
4. Users and group based policies


## Benefits
- Allows developers to focus on building the application as it provides all the logic for signing-in, login form, registration, password reset.
- Uses latest security standards for secure authentication and authorization. OAuth 2.0, SAML 2.0.
- Easily integrate Entra ID into on-premise Active Directory for a hybrid solution. Use Entra ID connect to sync users between on-premise and cloud, for easy IAM with already registered users into cloud applications.
- SSO across all cloud applications.

## Tiers

1. **Standard Tier**
    - Limited to 10 applications SSO
    - Self-service password **change** (after logged in).

2. **Premium - P1** - Typically needed for all enterprises.
    - Extends Standard tier.
    - Full Rebranding logon/registration page.
    - Self-service password **reset**
    - MFA.
    - Advanced security and reporting.

3. **Premium - P2**
    - Machine Learning based risk assessment of account activity to improve security.
    - "sudo" like temporary escalation of privilege to perform administrative tasks. Benefits are that it reduces number of admin permissions to be granted, and there is monitoring/logs of these activities.