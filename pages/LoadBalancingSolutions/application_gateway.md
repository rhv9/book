# Application Gateway

Application Gateway is a level 7 load balancer. It allows you to route traffic to backend pools based on HTTP, HTTPS and websockets.

It includes many features that an Application Delivery Controller (ADC) has:

- *SSL offloading*: The backend will receive the unencrypted data, reducing decryption load on backend servers.
- *Web Application Firewall (WAF)*: Analysis on HTTP packets for potential risks, which you can detect and even prevent (block).
- *Public and private IP*: or both.
- *Autoscaling* instances.
- *URL routing*: route traffic based on url. E.g. /images/ is routed to a specific backend pool vs /video/ is routed to another.
- Configure multiple backend pools and even route to on-premise or external servers.
- *Routing mode*: Round robin means circularly routing to each backend pool.

## Configuration

### General

**SKU**

There are:

- Standard
- Standard V2
- WAF
- WAF V2

WAF means it has WAF. Standard is without WAF

```diff
- What is the difference between V1 and V2
```

**Autoscaling**

Set a min and max instance count. Min count can be 0 so that no instances are running if there is no load. 

You can also disable it and have fixed instances running, but you would be a fool.

**Firewall**

Can enable or disable it and set whether to only do detection, or also block the risky traffic (prevention).

**Instance size**
Can select small, medium or large instance. This option is only available when choosing WAF.

### IP Address

Set a public ip, private or both. Standard V2 does not support public only and must use both.

### Backend pools

You can add one or more backend pools that you can route traffic to. A given backend pool can consist of Virtual Machines, IP addresses, Virtual Machine Scale Sets (VMSS), or App Services and a combination of them (I think?).

> Note: Adding VM and App Service to same backend pool cannot be done in Azure Portal, but instead can be achieved using PowerShell.

### Routing

There are three settings we need to create and configure which will make up a route plan. To make a route plan, you need a Listener, a Backend Pool and an HTTP setting. 

You can also route traffic based on path.

**Listener** 

This determines which packets should be grouped to be routed to a backend pool. 

You have to pick a unique combination of IP address, protocol (HTTP or HTTPS) and port number. Then all matching packets will be sent to a specific backend pool.

There is also support for multi-site routing. This is when you do Shared Web Hosting when there are more than one FQDN for a given IP Address. So you can choose to route based on a domain name than just every traffic on that IP Address.

> Note: Multi-site has precedence over basic.

**Backend Pool**

```diff
- to complete
```

**HTTP Setting**

```diff
- What is redirection?
- Cookie-based affinity I do not understand.
- Connection draining
```

