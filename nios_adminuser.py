#! /usr/bin/env python3
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: nios_adminuser

short_description: This module manages local admin users on Infoblox.

version_added: "1.0.0"

description: This module adds or updates Local admins in Infoblox.

options:
    user: 
        description: Name of the admin user you want to create or update.
        required: true
        type: str
    password: 
        description: Password for the admin user you are creating or updating (Can be used to update password for user)
        required: true
        type: str
    groups:
        description: Group(s) that the admin user is a member of.
        required: true
        type: str
    comment:
        description: Comment for the admin user.
        required: true
        type: str
    provider:
        description: A dict object containing connection details.
        type: list
        elements: dict
        suboptions:
          ibx_host:
            description: Specifies the DNS host name or address for connecting to the remote instance of NIOS.
            type: str
          ibx_username:
            description: Configures the username to use to authenticate the connection to the remote instance of NIOS.
            type: str
          ibx_password:
            description: Specifies the password to use to authenticate the connection to the remote instance of NIOS.
            type: str

author:
    - Andrew Heath (@anheath)
'''

EXAMPLES = r'''
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
'''

import urllib3
import sys
from infoblox_client import connector
from infoblox_client import objects
from ansible.module_utils.basic import AnsibleModule

def admin(module, ibx_host, ibx_username, ibx_password, user, password, groups, comment):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    opts = {'host': ibx_host, 'username': ibx_username, 'password': ibx_password}
    conn = connector.Connector(opts)
    admins = objects.Adminuser.create(conn, check_if_exists=True, update_if_exists=True, name=user, password=password, admin_groups=[groups], comment=comment)

def main():
    provider_spec = dict(
        ibx_host=dict(type='str', required=True),
        ibx_username=dict(required=True, type='str'),
        ibx_password=dict(required=True, type='str', no_log=True),
        )

    argument_spec = dict(
        user=dict(required=True, type='str'),
        password=dict(required=True, type='str', no_log=True),
        groups=dict(required=True, type='str'),
        comment=dict(required=False, type='str'),
        provider=dict(type='dict', required=True, options=provider_spec),
        )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        )

    ibx_host = module.params['provider']['ibx_host']
    ibx_username = module.params['provider']['ibx_username']
    ibx_password = module.params['provider']['ibx_password']
    user = module.params['user']
    password = module.params['password']
    groups = module.params['groups']
    comment = module.params['comment']

    result = admin(module, ibx_host, ibx_username, ibx_password, user, password, groups, comment)
    module.exit_json(changed=True )

if __name__ == "__main__":
    main()
