# Virtual Machine Scale Sets

When we need to scale Virtual Machines in and out based on demand, we can use Virtual Machine Scale Sets. It is a service that allows you to group a set of VM instances into a scale set has configured scale in and out settings.

On creation, you can specify the VM configuration similar to when creating an individual VM. This includes storage, networking, advanced, management, extensions, and more.

You can also create a Load Balancer directly there or add it as a backend pool after creation.

#### Scaling

Scale in and scale out configuration is similar to a Web App Service Plan. A simple solution may be to increase instance when average CPU load is greater than 80% and scale in (reduce instances) when average load is less than 15%.

You can specify the min and max instance count as well.

Another important option when scaling in and out is which VM to delete when scaling back in. We can specify to delete the newest  created instance or delete in order of first creation.

#### Types of VMSS

There are two main types of VMSS, flexible and uniform.

*Uniform* - Uniform means all VMs in the scale set are exactly the same. Each has the same size and power.

*Flexible* - You will have the ability to add your own created VMs to the pool.