# niox_adminuser
---
#### Manages Infoblox admin users

Version added: 1.0.0

- [Synopsis](#synopsis)
- [Parameters](#parameters)
- [Notes](#notes)
- [Examples](#examples)
- [Status](#status)
- [Authors](#authors)
## Synopsis
---
  - This module allows for the management of Infoblox Local admin accounts.

## Parameters
---

| Parameter                          | Comments                                                                                           |
| ---------------------------------- | -------------------------------------------------------------------------------------------------- |
| user<br>string/required            | Name of the admin user you want to create or update                                                |
| password<br>string/required        | Password for the admin user you are creating or updating (Can be used to update password for user) |
| groups<br>list/required            | Group(s) that the admin user is a member of                                                        |
| comment<br>string                  | Comment for the admin user.                                                                        |
| provider<br>dictionary             | A dict object containing connection details.                                                       |
| -> ibx_hosts<br>string/required    | Specifies the DNS host name or address for connecting to the remote instance of NIOS.              |
| -> ibx_username<br>string/required | Configures the username to use to authenticate the connection to the remote instance of NIOS.      |
| -> ibx_password<br>string/required | Specifies the password to use to authenticate the connection to the remote instance of NIOS.       |
## Notes
---
Note
- Tested on an Infoblox applience running Version: 8.6.3.

## Examples
---
```yaml
- name: Create new user
  nios_adminuser:
    user: test-user
    password: password
    groups: test-group
    provider:
      ibx_host: host.example.com
      ibx_username: user
      ibx_password: password
- name: Add a comment to user
  nios_adminuser:
    user: test-user
    password: password
    groups: test-group
    comment: Test comment
    provider:
      ibx_host: host.example.com
      ibx_username: user
      ibx_password: password
```

## Status
---

## Authors
---
- Andrew Heath ([@anheath](https://gitlab.cee.redhat.com/anheath))
