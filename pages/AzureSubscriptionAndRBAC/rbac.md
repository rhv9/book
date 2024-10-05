# RBAC

Managing access to resources. Capability to grant permissions to Microsoft Entra ID users, groups and services.

Some default roles include:
1. Owner - everything
2. Contributor - create and manage all types of resources, but can't grant access to other users and groups.
4. Reader - only read

Some roles are categorised as administrator role.

*Assignable Scopes* determines where the role can be assigned. We can make a role work in a subscription, or more specific with resourge group, or even more specific with a resource.

## Role Definition

Is a JSON formatted file that determines what permissions are given, to whom it is assigned to, and the scope at which it is assigned. 

There are three components that make up a Role definition:

1. Permissions
2. Role assignments
3. Scope

The permissions consist of ```actions```, ```not actions```, ```data actions```, and ```not data actions```.

Role, whether custom or built-in can be assigned to users, groups or service principals.

The scope can start from as high as the root (management group) all the way down to individual resources. This is seen when in Azure Portal, the service has a Identity Access (IAM) tab.

### Actions and Not Actions

We can grant actions or remove actions (Not actions) like such:

Examples
- ```*/read``` grants access to read for all resource types of all Azure resource providers
- ```Microsoft.Computer/*``` grants access to all operations for all resource types in the Microsoft.Compute resource provider
- ```Microsoft.Network/*/read``` grants access to read operations to all resource types in the Microsoft.Network resource provider.

We can see how the in-built roles are created with what actions and not actions are defined

- Contributor role has action everything but some not actions to prevent managing other users.

### Data Actions and Not Data Actions

These are permissions that has to do with the data of a service. For example in Storage Account, you can give permissions to access data in containers.
