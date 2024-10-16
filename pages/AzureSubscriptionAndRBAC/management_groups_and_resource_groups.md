# Management Groups and Resource Groups

Management Groups are a layer above subscriptions which is used as a scope for giving RBAC permissions, defining policies and creating Budget. 

The whole point of Management Groups is to manage more than one subscription. It gives you the layer above multiple subscriptions to assign security, policies and budgeting.

All subsequent child Management Groups, Resource Groups, Subscriptions or resourcces will inherit these from the parent.

This allows for ease of management of roles and policies across multiple subscriptions.