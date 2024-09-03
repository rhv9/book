# API Management Services

> u-developers = the users of our service are developers.

API Mangament services is a service you can deploy on top of your hosted APIs to allow you to manage them. Tasks you may want to manage include providing API documentation to u-developers, a platform to test the API, rate limiting, quotas, collecting telemetry about API or subscribing to our API.

This service can be connected to both self hosted on-premise web API or Azure's Web App service.

All users of the API will now instead use this new gateway API rather than directly communicating with the backend.

## Benefits of using API Management

1. Secure and optimize API
2. Collect telemetry and logs about API use.
3. perform transformative tasks like convert from XML to JSON.
4. Easier to use learn to use API.

## Main terminology used in API Management Services

A **product** is a group of API/operations. A u-developer can subscribe to use a product.

**Groups** allows you to group users to restrict what they may be able to do with the API.

## Components of API Management services

1. API Gateway: This is the gateway that is connected to the backend API. Accepts API calls and routes them to the backend. Collects telemetry. Allows adding policies to perform a set of tasks on an API call, e.g rate limiting, quotas. Caching
2. Developer portal: This is a website generated that you can modify. It provides a place where you can view the API documentation, subscribe to API or test API directly in the portal.