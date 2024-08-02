#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2024, Marco Noce <marco.X0178421@gmail.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: svcs_attr_facts
author:
    - Marco Noce (@NomakCooper)
description:
    - Gathers facts about Solaris SMF attribute for a specific services by svcs.
    - This module currently supports SunOS Family, Oracle Solaris 10/11.
requirements:
  - svcs
short_description: Gathers facts about solaris SMF attribute for a specific services.
notes:
  - |
    This module shows the list of attribute of solaris SMF service.
'''

EXAMPLES = r'''
- name: run custom svcs module
  svcs_attr_facts:
    fmri: "svc:/network/smtp:sendmail"
    alias: sendmail

- name: set fact for print
  set_fact:
    sendmail_state: "{{ ansible_facts.sendmail_attr| map(attribute='state') | first }}"
    sendmail_logfile: "{{ ansible_facts.sendmail_attr| map(attribute='logfile') | first }}"

- name: print state and logfile of sendmail service
  debug:
    msg: "sendmail service is {{sendmail_state}}. Check logfile {{sendmail_logfile}} for info."

'''

RETURN = r'''
ansible_facts:
  description: Dictionary containing the attribute of SMF service
  returned: always
  type: complex
  contains:
    'alias'_list:
      description: A list of attribute of SMF service. ( the list name is created from the alias entered as a parameter )
      returned: always
      type: list
      contains:
        fmri:
          description: The FMRI of the service instance.
          returned: always
          type: str
          sample: "svc:/network/smtp:sendmail"
        name:
          description: The complite name of service.
          returned: always
          type: str
          sample: "sendmail SMTP mail transfer agent"
        enabled:
          description: If the service instance is enabled or disabled.
          returned: always
          type: str
          sample: "true"
        state:
          description: The current state of service instance.
          returned: always
          type: str
          sample: "online"
        next_state:
          description: The next state of the service.
          returned: always
          type: str
          sample: "none"
        state_time:
          description: date and time of the last transaction of the current status.
          returned: always
          type: str
          sample: "August  1, 2024 at  6:34:29 PM CEST"          
        logfile:
          description: The log file of service instance.
          returned: always
          type: str
          sample: "/var/svc/log/network-smtp:sendmail.log"           
        restarter:
          description: The master restarter daemon for SMF
          returned: always
          type: str
          sample: "svc:/system/svc/restarter:default"             
        contract_id:
          description: The primary contract ID for the service instance.
          returned: always
          type: str
          sample: "133 "          
        manifest:
          description: The .xml manifest file of the service instance.
          returned: always
          type: str
          sample: "/lib/svc/manifest/network/smtp-sendmail.xml"         
        dependency(n):
          description: The dependency service. ( the number of dependencies changes according to the service )
          returned: always
          type: str
          sample: "optional_all/none svc:/system/filesystem/autofs (online)"                                                 
'''

import re
import platform
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.basic import AnsibleModule


def smf_parse(raw):

    results = list()

    lines = raw.splitlines()
    for line in lines:
        cells = line.split(None, 1)
        param, value = cells

        result = {
                param: value,
            }
        
        results.append(result)

    return results

def main():
    module = AnsibleModule(
        argument_spec=dict(
            fmri=dict(type='str', required=True),
            alias=dict(type='str', required=True),
        ),
        supports_check_mode=True,
    )

    smf = module.params['fmri']
    svcname = module.params['alias']
    command_args = ['-l', smf]
    commands_map = {
        'svcs': {
            'args': [],
            'parse_func': smf_parse
        },
    }
    
    commands_map['svcs']['args'] = command_args

    if platform.system() != 'SunOS':
        module.fail_json(msg='This module requires SunOS.')

    result = {
        'changed': False,
        'ansible_facts': {
            svcname + '_attr': [],
        },
    }

    try:
        command = None
        bin_path = None
        for c in sorted(commands_map):
            bin_path = module.get_bin_path(c, required=False)
            if bin_path is not None:
                command = c
                break

        if bin_path is None:
            raise EnvironmentError(msg='Unable to find any of the supported commands in PATH: {0}'.format(", ".join(sorted(commands_map))))

        
        args = commands_map[command]['args']
        rc, stdout, stderr = module.run_command([bin_path] + args)
        if rc == 0:
            parse_func = commands_map[command]['parse_func']
            results = parse_func(stdout)
            
            # time to merge
            merged = {}
            # counter for dependeny duplicate
            ck = 0

            for svcsl in results:
              for k, v in svcsl.items():                  
                  if k.startswith("dependency"):
                    ck += 1              
                    join = {
                        
                        k + str(ck): v,

                    }
                  else:                    
                    join = {
                        
                        k: v,

                    }                    

                  merged.update(join)

            result['ansible_facts'][svcname + '_attr'].append(merged)
    except (KeyError, EnvironmentError) as e:
        module.fail_json(msg=to_native(e))

    module.exit_json(**result)


if __name__ == '__main__':
    main()
