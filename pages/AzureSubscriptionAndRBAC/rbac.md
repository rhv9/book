# RBAC

Managing access to resources. Capability to grant permissions to Microsoft Entra ID users, groups and services.

Some default roles include:
1. Owner - everything
2. Contributor - create and manage all types of resources, but can't grant access to other users and groups.
4. Reader - only read

*Assignable Scopes* determines where the role can be assigned. We can make a role work in a subscription, or more specific with resourge group, or even more specific with a resource.

### Actions and Not Actions

We can grant actions or remove actions (Not actions) like such:

Examples
- ```*/read``` grants access to read for all resource types of all Azure resource providers
- ```Microsoft.Computer/*``` grants access to all operations for all resource types in the Microsoft.Compute resource provider
- ```Microsoft.Network/*/read``` grants access to read operations to all resource types in the Microsoft.Network resource provider.

We can see how the in-built roles are created with what actions and not actions are defined

- Contributor role has action everything but some not actions to prevent managing other users.
