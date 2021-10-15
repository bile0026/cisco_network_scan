#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Zachary Biles <zacharybiles@gmail.com>
# GNU Affero General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/agpl-3.0.txt)

from ansible.errors import AnsibleError
import urllib3
import json

DOCUMENTATION = r"""
  name: mac_information
  short_description: Get Mac address vendor information
  description:
    - Returns vendor information from maclookup.app api to find vendor from mac address.
  version_added: "0.1.0"
  options:
"""
EXAMPLES = r"""
"""
RETURN = r"""
  {{ key }}:
    vendor:
"""


class FilterModule(object):  # 1

    def filters(self):  # 2
        return {
            'get_mac_info': self.get_mac_info,
        }  # 4

    def get_mac_info(self, mac_address, info_to_get):  # 3
        http = urllib3.PoolManager()
        mac_info = http.request(
            'GET', 'https://api.maclookup.app/v2/macs/' + mac_address)
        mac_info = json.loads(mac_info.data.decode('utf-8'))
        try:
            return mac_info[info_to_get]
        except:
            return "none"
