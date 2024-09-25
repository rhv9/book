# Scaling App Service Plan

Objectives:
1. What is vertical and horizontal scaling.
2. Knowing when to scale vertically and horizontally.
3. Rule-based scaling and automatic scaling.

## Scaling

Scaling is about increasing the power/capacity of our app based on the demand to ensure high availability and reduce costs. This can be achieved in 2 ways, vertical and horizontal scaling.

Vertical scaling is about increasing the vCPUs and memory. This will be like going from Standard S1 to Standard S2. Azure *doubles* the vCPU and memory for every tier higher you go. So for Standard S1, vCPU = 1, S2 = 3.5 vCPU, and S3 = 7 vCPU.

Horizontal scaling is the number of instances of the VM. It is duplicating the VM. Copy and paste. Nothing more to say.

## What to consider?

### Costs

Costs are an important topic when deciding between scaling vertically or horizontally or both. Azure SKU costs are double for every tier higher you go. So *double* the CPU and memory means *double* the cost. 

And double the instances also means *double* the cost. So choosing the right option is very important.

### Maximum Concurrent Requests

Another thing to consider is the number of connections each CPU can handle. For lower tiers, one CPU can handle 7,500 connections for Standard tier. A Basic SKU can only handle 350 concurrent requests (which is typically only for dev/testing and not production).

> Note: I don't really know the exact numbers, google it. It is more about the point than the precision of what I speak.

### Bottleneck

The decision on whether to scale vertically or horizontally is about what is the bottleneck of the application. Does your application require a lot of memory and CPU processing power? Or it is low and instead there are a lot of simultaneous connections that are bottlenecked by other metrics (network connections, disk access).

If you are running heavy algorithms and use a lot of memory, then scaling CPU and memory is the right choice. If it is more about fetching data and number of active users, then increasing the instance counts to support more users in parallel is the better choice.

## Scaling options

1. **Manual scaling** - set it manually. ***Vertical scaling can only be done manually I think***.

2. **Rule-based scaling** - Write rules that govern when you scale out and scale in.

You can have a default profile which says what is the instance count by default.

Then you can add a profile for scaling in and out. You can add a rule based on metrics, e.g average CPU usage percentage over a period of time to scale instance count by a specific amount, a specific number of times.

Some Rule factors:

    1. Scaling in or out
    2. Instance count to increase or decrease.
    3. The metric the rule is applied on.
        - What period of time the average is calculated by
        - Time grain ie how many times the value should be polled.
        - Cooldown after scaling up.
    4. The days of the week this is active.
    5. For what period of time this profile is active.

3. **Automatic scaling** is a new feature that automatically scales VMs. Azure manages the metrics to determine when to scale in or out. All you have to do it set limits on the instances.

This is **only** supported for *Premium SKU*.

You can configure:

    1. Burst limit. If surge of requests, what 
        you can add a burst limit to instance counts.
    2. Default active instance count.
    3. Maximum instance count.

    

