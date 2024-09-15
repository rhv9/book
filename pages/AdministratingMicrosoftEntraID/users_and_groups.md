# Users and Groups

We can create **users** on an azure tenant with a verified domain name on the EntraID. Users can also be created in **batch** using a ```.csv``` file generated from portal.

We can also invite guests into the 

## Groups

Owner is responsible for adding users. EntraID also supports requesting to join a group, which the owner can accept or deny.

### Dynamic users

We can automatically add or remove users from a group using dynamic users list. This list contains a set of checks and if (all?) properites of users match, they will automatically be added or removed from the group.

```diff
- is it all checks must pass or each
```

### Types of groups

We have two types of groups

1. Microsoft 365 Groups:

These can have only users. Good for make collaboration easier between members of the group through shared drive, calendar.

2. Security Groups

These can have users and devices.