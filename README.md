<meta name="author" content="Marco Noce">
<meta name="description" content="Gathers facts about Solaris SMF attribute for a specific services by svcs.">
<meta name="copyright" content="Marco Noce 2024">
<meta name="keywords" content="ansible, module, solaris, svcs, attribute, smf, service">

<div align="center">

![Ansible Custom Module][ansible-shield]
![Oracle Solaris][solaris-shield]
![python][python-shield]
![license][license-shield]

</div>


### svcs_attr_facts ansible custom module
#### Gathers facts about Solaris SMF attribute for a specific services by svcs.

#### Description :

<b>svcs_attr_facts</b> is a custom module for ansible that creates an ansible_facts containing the attribute list of specific SMF services on a SunOS/Oracle Solaris host

#### Repo files:

```
├── /library                
│   └── svcs_attr_facts.py   ##<-- python custom module
└── svcs_attr.yml            ##<-- ansible playbook example
```

#### Requirements :

*  This module supports SunOS/Oracle Solaris only
*  The SMF services info are gathered from the [svcs] command

#### Parameters :

|Parameter|Type  |Required|Sample                      |Comment                                                                                                                 |
|---------|------|--------|----------------------------|------------------------------------------------------------------------------------------------------------------------|
|fmri     |string|True    |"svc:/network/smtp:sendmail"|The FMRI of the service instance                                                                                        |
|alias    |string|True    |"sendmail"                  |Service alias, a name of your choice which will then be automatically assigned to the dict object name ( sendmail_attr )|

#### Attributes :

|Attribute |Support|Description                                                                         |
|----------|-------|------------------------------------------------------------------------------------|
|check_mode|full   |Can run in check_mode and return changed status prediction without modifying target.|
|facts     |full   |Action returns an ansible_facts dictionary that will update existing host facts.    |

#### Examples :

#### Tasks
```yaml
---
- name: Gather attribute of sendmail fmri
  svcs_attr_facts:
    fmri: "svc:/network/smtp:sendmail"
    alias: sendmail

- name: set fact for print
  set_fact:
    sendmail_state: "{{ ansible_facts.sendmail_attr| map(attribute='state') | first }}"
    sendmail_logfile: "{{ ansible_facts.sendmail_attr| map(attribute='logfile') | first }}"

- name: print state and logfile attribute of sendmail service
  debug:
    msg: "sendmail service is {{sendmail_state}}. Check logfile {{sendmail_logfile}} for info."

```
#### 'alias'_attr facts:
```json
  "ansible_facts": {
    "sendmail_attr": [
      {
        "fmri": "svc:/network/smtp:sendmail",
        "name": "sendmail SMTP mail transfer agent",
        "enabled": "true",
        "state": "online",
        "next_state": "none",
        "state_time": "August  1, 2024 at  6:34:29 PM CEST",
        "logfile": "/var/svc/log/network-smtp:sendmail.log",
        "restarter": "svc:/system/svc/restarter:default",
        "contract_id": "133 ",
        "manifest": "/lib/svc/manifest/network/smtp-sendmail.xml",
        "dependency1": "optional_all/none svc:/system/filesystem/autofs (online)",
        "dependency2": "require_all/refresh file://localhost/etc/mail/sendmail.cf (online)",
        "dependency3": "require_all/refresh file://localhost/etc/nsswitch.conf (online)",
        "dependency4": "require_all/none svc:/system/filesystem/local (online)",
        "dependency5": "optional_all/refresh svc:/system/identity:domain (online)",
        "dependency6": "require_all/refresh svc:/milestone/name-services (online)",
        "dependency7": "require_all/none svc:/network/service (online)",
        "dependency8": "optional_all/none svc:/system/system-log (multiple)"
      }
    ]
  },
```
#### debug output from example :
```
TASK [print state and logfile attribute of sendmail service] *****************************************
ok: [sol11host] => {
    "msg": "sendmail service is online. Check logfile /var/svc/log/network-smtp:sendmail.log for info."
}
```
#### Returned Facts :

*  Facts returned by this module are added/updated in the hostvars host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.
*  Attributes change according to the service selected

|Key          |Type  |Description                                                                            |Returned|Sample                                                    |
|-------------|------|---------------------------------------------------------------------------------------|--------|----------------------------------------------------------|
|'alias'_attr |list / elements=string|SMF Services list                                                      |        |                                                          |
|fmri         |string|The FMRI of the service instance.                                                      |always  |"svc:/network/smtp:sendmail"                              |
|name         |string|The complite name of service.                                                          |always  |"sendmail SMTP mail transfer agent"                       |
|enabled      |string|If the service instance is enabled or disabled.                                        |always  |"true"                                                    |
|state        |string|The current state of service instance.                                                 |always  |"online"                                                  |
|next_state   |string|The next state of the service.                                                         |always  |"none"                                                    |
|state_time   |string|Date and time of the last transaction of the current status.                           |always  |"August  1, 2024 at  6:34:29 PM CEST"                     |
|logfile      |string|The log file of service instance.                                                      |always  |"/var/svc/log/network-smtp:sendmail.log"                  |
|restarter    |string|The master restarter daemon for SMF.                                                   |always  |"svc:/system/svc/restarter:default"                       |
|contract_id  |string|The primary contract ID for the service instance.                                      |always  |"133 "                                                    |
|manifest     |string|The .xml manifest file of the service instance.                                        |always  |"/lib/svc/manifest/network/smtp-sendmail.xml"             |
|dependency(n)|string|The dependency service. ( the number of dependencies changes according to the service )|always  |"optional_all/none svc:/system/filesystem/autofs (online)"|

## Integration

1. Assuming you are in the root folder of your ansible project.

Specify a module path in your ansible configuration file.

```shell
$ vim ansible.cfg
```
```ini
[defaults]
...
library = ./library
...
```

Create the directory and copy the python modules into that directory

```shell
$ mkdir library
$ cp path/to/module library
```

2. If you use Ansible AWX and have no way to edit the control node, you can add the /library directory to the same directory as the playbook .yml file

```
├── root repository
│   ├── playbooks
│   │    ├── /library                
│   │    │   └── svcs_attr_facts.py      ##<-- python custom module
│   │    └── your_playbook.yml           ##<-- you playbook
```   

[ansible-shield]: https://img.shields.io/badge/Ansible-custom%20module-blue?style=for-the-badge&logo=ansible&logoColor=lightgrey
[solaris-shield]: https://img.shields.io/badge/oracle-solaris-red?style=for-the-badge&logo=oracle&logoColor=red
[python-shield]: https://img.shields.io/badge/python-blue?style=for-the-badge&logo=python&logoColor=yellow
[license-shield]: https://img.shields.io/github/license/nomakcooper/svcs_attr_facts?style=for-the-badge&label=LICENSE


[svcs]: https://docs.oracle.com/cd/E86824_01/html/E54763/svcs-1.html
