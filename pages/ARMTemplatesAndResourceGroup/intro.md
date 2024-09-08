# ARM Templates and Resource Group

## Resource Providers

In Azure, resources/services and operations are provided by Resource Providers. Why is this important. How does this make reasoning about ARM templates easier? We write ARM Templates based on the resource type and provider.

```<resource-provider>/<resource-type>```

## ARM Templates

Azure Resource Manager is the new way in which resources are created in Azure. The old method that Azure Portal and Azure PowerShell used was *Service Management API*. The problem with the old system is of it being serially executed, each call only creates a single resource, and having to write custom scripts to check if resource exists or not before performing tasks. 

Azure Resource Manager Templates is a declarative way to create a group of resources. The template is a JSON formatted file. 

- One of the benefits of templates is it can be parameterised so that the same template can have different configurations for different purposes, e.g production, staging, dev, testing, etc.

- ARM templates also orchestrates creation of multiple resources so that resources can be easily created in parallel. 
- Resources can have dependencies to control the order of creation if a particular resource requires another resource to exist before its creation.

## Ways to extract ARM Templates

1. We can extract the ARM Template from a deployment made in a resource group.
2. Configure a creation of a resource and extract template at the end.
3. Export a resource group into a template. This recreates the state of all the resources in a resource group at the time of export. 
    - Easily recreate the exact same resource group. Maybe you want to save costs and are not using the resources now so you can create the same resources later with this.