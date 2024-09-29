# Traffic Manager

It is a DNS-based load balancer that allows you to route traffic across global Azure regions.

DNS-based load balancer means that it only is used to evaluate the IP Address. If it was a load balancer, traffic flows with load balancer as the middle man. Whereas Traffic manager will evaluate which endpoint it should give, then traffic is directly routed to the endpoint.

Traffic Managers can be nested.

## Endpoints

Here we can add each individual service endpoint. Based on routing method, different endpoint will be reached to the client. 

If routing method is performance based, then it is decided based on RTT latency which is precalculated for all IP ranges. Therefore, it will route traffic to the endpoint with lowest latency.

> The public IP Addresses must have a FQDN.

## Configuration

**Routing Method** Determines how to choose the endpoint when trying to connect to the global traffic managers IP. 

- Performance = latency
- Geographic = geographic
- Priority = typically for disaster recovery/if highest priorty is down.
- Weighted = share load based on weighting. Good for canary deployment.


