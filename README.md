# cisco_network_scan

Scans your cisco devices looking for access ports with more than 2 mac addresses learned. If this is the case, there's likely an unmanaged device connected.

## How to use

Install `cisco.ios` collection with `ansible-galaxy collection install -r collections/requirements.yml`.

Define `mac_count` to 8 if you want to report on interfaces with more than 2 mac addresses learned. (only cares about access interfaces. Trunk interfaces are assumed to have lots of mac addresses) Increment by 1 to allow additional mac addresses per interface.

Run `scan_network.yml` playbook. `ansible-playbook -i hosts scan_network.yml`

## Requirements
Requires Ansible version 2.10.X+ due to jinja templating changes. Will hopefully get this resolved to work with pre-2.10.X versions at some point.

Install pip requirements `pip install -r requirements.txt`

Clone the ntc-ansible git repository into this directory `git clone https://github.com/networktocode/ntc-ansible.git --recursive`

## Reporting
Reports are generated by setting `generate_report` to true.

If you want reports emailed i.e. you run this nightly and want a daily report of non-compliance, set these variables.

```
smtp_server: smtp.example.com
smtp_port: 25
email_addresses:
  - user@example.com
from_email: from@example.com
```

### Include vendor info in report
By default vendor info is looked up for each mac address found on a "suspicious interface". Set `include_vendor_info` to false to leave this out of the report.

Also uses https://maclookup.app API to lookup the mac address vendor information and output it in the report. By default the free (non-authenticated API allows 2 requests per second and a total of 10,000 requests per-day). Other types of data can be put in the report by editing the string passed to the `get_mac_info` filter. Allowed values are `mac, company, address, blockStart, blockEnd, blockSize, blockType, updated, isRand, isPrivate` (default is company). For more information see the maclookup.app documentation here https://maclookup.app/api-v2/documentation.

Eventually, I plan to add authentication to allow for additional requests per-second/day, and other error handling and improvements to the filter plugin. For now, quick and dirty did the trick for me.

## Issues/bugs/suggestions
Please open an issue if you find bugs or have suggestions.
