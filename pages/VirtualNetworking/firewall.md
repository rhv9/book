# Firewall

How is it different from NSG? We cannot block websites based on domain names. NSG's only use the 5 tuple (SRC IP, SRC Port, DEST IP, DEST Port, Protocol).

Benefits of blocking based on domain name include, but not limited to:
1. Only allowing certain websites used in corporate work
2. Blocking a list of banned websites

## What can you configure?

1. Application rules: FQDNs? Block based on domain names
2. Network rules: essentially NSG
3. NAT rules: forwarding requests on a port of firewall to a particular (IP, port)

## Key features

1. 

## Creating firewall

Some notes when creating firewall

- Firewall management: Firewall policy is reusable set of rules.
- 
```diff
- what is forced tunneling?
- application rules/FQDNs are confusing
```

## Some points when deploying firewall

- Make sure subnets have user defined route table to route any outbound traffic via firewall.
- Do not make VMs directly accessible to the internet. Instead, add NAT rule to map 

## Firewall policy

You can attach this policy to configure any firewall, across regions (irregardless of where it is created). 

It has Rule collections groups which contains rule collections which contain rules.

Rule collection groups and rule collections have priorities.

Can attach parent policy to inherit from.

Typically use Network rules to allow or block certain DNS.

