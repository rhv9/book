# Azure Policy

Azure Policy is a service that allows you to govern resources across Azure services to ensure compliance with standards and organisation policies. It allows you to create, assign and manage these policies.

When a policy is in action, governance will be ensured in many ways:

1. New resources not following policies will be denied
2. Remediation action: Automatically perform a wide scale reconfiguration of resources that do not meet the policy.
3. Compliance monitor


At a high level it is about managing the combination of *Security Principal* + *Role assignment* + *Scope*. Remember that scopes are inheritable. BIG thing to remember is you cannot break inheritance.

## Policy Initiative vs Initiative Definition

Policy Initiative is a single policy whereas Initiative Definition is a group of policies.


## Creating policies

