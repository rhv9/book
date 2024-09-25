# Lock, Quotas, Tag, Cost, Advisor

These are other important ways to govern your Azure services.

## Lock

Locks are a way to mark Azure services as either delete only or read only. These are helpful in ensuring resources are not altered or deleted accidentally.

The scope they can be applied goes from as high level as Subsciptions, to then Resource Groups and then down to individual resources.

Locks are inherited so if a Resource Group has a lock, then it applies to all resources under it.

## Quotas

Each subscription has a max quota on how many of each resource you can create. You can create a request to Azure support to increase it if needed, within reasonable reasons.

You can find this under the subscription, then find Quotas.

## Tags

Tags are a way to add key value pair tags to individual resources, resource groups or even subscriptions.

They are a great way to filter resources for various purposes. One purpose may be to add an "env" variable that can be assigned "dev", "test", or "prod" to be able to tell what environment the resource is used for.

Then you can filter the resources by tag to gain insight into the costs for each environment.

> Note: Tags are not inherited so it has to be added to each individual resource.

Tag name = 512 bytes, tag values = 256 bytes.

> Also Note: In storage account, size of tag name and value is halfed.

## Cost

Costs can be viewed at Resource group level or subscription level. 

There are also costs for individual services but those depend on the service.

#### Cost alerts and budgeting

There is no way direct way to stop resources if a budget is reached under cost settings. However, we can add **Cost Alerts** so that alerts are generated. Then we can capture these alerts as events in Event Hub and carry out any action such as stopping resources.

Budgets can be added to resources, although idk what they are.

## Advisor

Advises you to reduce costs, improve security, reliability, etc.