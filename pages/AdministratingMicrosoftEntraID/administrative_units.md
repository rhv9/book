# Administrative Units

> Note: The user requies a Entra ID P2 License to be an administrative unit. So each administrative user in the administrative unit needs the license.

Administrative Units are a collection of users and groups with admin users who has privileges to perform specific assigned actions based on the assigned administrative roles.

### Built-in Roles

1. Authentication Administrator
2. Password Administrator - Reset password for all users in the administrative unit who are not admins.
3. User Administrator - Can manage limited number of admins
4. Group Administrator
5. Helpdesk Administrator
6. License Administrator

> Note: The trick question is remembering that admin cannot use privilege actions on other admins

```diff
- Which admin roles cannot perform privileged tasks on other admins?
```

The benefit is that the admin's scope is can only administer within the scope of the AU. This way, you can easily assign certain common IT admin work in larger organisations, across multiple groups. Whereas defining admin role within group scope means that you can only administrate within that group.