# -*- coding: utf-8 -*-
#  Copyright (c) 2022 - 2022 Ricardo Bartels. All rights reserved.
#
#  fritzinfluxdb.py
#
#  This work is licensed under the terms of the MIT license.
#  For a copy, see file LICENSE.txt included in this
#  repository or visit: <https://opensource.org/licenses/MIT>.

from fritzinfluxdb.common import grab
from fritzinfluxdb.classes.fritzbox.service_definitions import lua_services


def prepare_json_response_data(response):
    """
    handler to prepare returned json data for parsing
    """

    return response.json()


lua_services.append({
        "name": "VPN Users",
        "os_min_versions": "7.29",
        "os_max_versions": "7.38",
        "method": "POST",
        "params": {
            "page": "shareVpn",
            "xhrId": "all",
            "xhr": 1,
        },
        "response_parser": prepare_json_response_data,
        "value_instances": {
            "myfritz_host_name": {
                "data_path": "data.vpnInfo.server",
                "type": str
            },
            "vpn_type": {
                "data_path": "data.vpnInfo.type",
                "type": str
            },
            "vpn_user_connected": {
                "data_path": "data.vpnInfo.userConnections",
                "type": dict,
                "next": {
                    "type": str,
                    "value_function": lambda data: data.get("connected"),
                    "tags_function": lambda data: {"name": data.get("name"), "vpn_type": "IPSec"}
                },
                "exclude_filter_function": lambda data: not isinstance(grab(data, "data.vpnInfo.userConnections"), dict)
            },
            "vpn_user_active": {
                "data_path": "data.vpnInfo.userConnections",
                "type": dict,
                "next": {
                    "type": str,
                    "value_function": lambda data: data.get("active"),
                    "tags_function": lambda data: {"name": data.get("name"), "vpn_type": "IPSec"}
                },
                "exclude_filter_function": lambda data: not isinstance(grab(data, "data.vpnInfo.userConnections"), dict)
            },
            "vpn_user_virtual_address": {
                "data_path": "data.vpnInfo.userConnections",
                "type": dict,
                "next": {
                    "type": str,
                    "value_function": lambda data: data.get("virtualAddress"),
                    "tags_function": lambda data: {"name": data.get("name"), "vpn_type": "IPSec"}
                },
                "exclude_filter_function": lambda data: not isinstance(grab(data, "data.vpnInfo.userConnections"), dict)
            },
            "vpn_user_remote_address": {
                "data_path": "data.vpnInfo.userConnections",
                "type": dict,
                "next": {
                    "type": str,
                    "value_function": lambda data: data.get("address"),
                    "tags_function": lambda data: {"name": data.get("name"), "vpn_type": "IPSec"}
                },
                "exclude_filter_function": lambda data: not isinstance(grab(data, "data.vpnInfo.userConnections"), dict)
            },
            "vpn_user_num_active": {
                "type": int,
                "value_function": (lambda data:
                                   len(
                                       [x for x in grab(data, "data.vpnInfo.userConnections", fallback=dict()).values()
                                        if x.get("connected") is True]
                                   )
                                   ),
                "tags": {
                    "vpn_type": "IPSec"
                },
                "exclude_filter_function": lambda data: not isinstance(grab(data, "data.vpnInfo.userConnections"), dict)
            }
        }
    }
)

lua_services.append({
        "name": "VPN Users - IPSec",
        "os_min_versions": "7.39",
        "method": "POST",
        "params": {
            "page": "shareVpn",
            "xhrId": "all",
            "xhr": 1,
        },
        "response_parser": prepare_json_response_data,
        "value_instances": {
            "myfritz_host_name": {
                "data_path": "data.init.server",
                "type": str
            },
            "vpn_type": {
                "data_path": "data.init.type",
                "type": str
            },
            "vpn_user_connected": {
                "data_path": "data.init.userConnections",
                "type": dict,
                "next": {
                    "type": str,
                    "value_function": lambda data: data.get("connected"),
                    "tags_function": lambda data: {"name": data.get("name"), "vpn_type": "IPSec"}
                },
                "exclude_filter_function": lambda data: not isinstance(grab(data, "data.init.userConnections"), dict)
            },
            "vpn_user_active": {
                "data_path": "data.init.userConnections",
                "type": dict,
                "next": {
                    "type": str,
                    "value_function": lambda data: data.get("active"),
                    "tags_function": lambda data: {"name": data.get("name"), "vpn_type": "IPSec"}
                },
                "exclude_filter_function": lambda data: not isinstance(grab(data, "data.init.userConnections"), dict)
            },
            "vpn_user_virtual_address": {
                "data_path": "data.init.userConnections",
                "type": dict,
                "next": {
                    "type": str,
                    "value_function": lambda data: data.get("virtualAddress"),
                    "tags_function": lambda data: {"name": data.get("name"), "vpn_type": "IPSec"}
                },
                "exclude_filter_function": lambda data: not isinstance(grab(data, "data.init.userConnections"), dict)
            },
            "vpn_user_remote_address": {
                "data_path": "data.init.userConnections",
                "type": dict,
                "next": {
                    "type": str,
                    "value_function": lambda data: data.get("address"),
                    "tags_function": lambda data: {"name": data.get("name"), "vpn_type": "IPSec"}
                },
                "exclude_filter_function": lambda data: not isinstance(grab(data, "data.init.userConnections"), dict)
            },
            "vpn_user_num_active": {
                "type": int,
                "value_function": (lambda data:
                                   len(
                                       [x for x in grab(data, "data.init.userConnections", fallback=dict()).values()
                                        if x.get("connected") is True]
                                   )
                                   ),
                "tags": {
                    "vpn_type": "IPSec"
                },
                "exclude_filter_function": lambda data: not isinstance(grab(data, "data.init.userConnections"), dict)
            }
        }
    }
)

lua_services.append({
        "name": "VPN Users - WireGuard",
        "os_min_versions": "7.39",
        "method": "POST",
        "params": {
            "page": "shareWireguard",
            "xhrId": "all",
            "xhr": 1,
        },
        "response_parser": prepare_json_response_data,
        "value_instances": {
            # currently covered by VPN IPSec service
            # "myfritz_host_name": {
            #    "data_path": "data.init.server",
            #    "type": str
            # },
            # "vpn_type": {
            #    "data_path": "data.init.type",  # currently falsely returns "IPSec Xauth PSK"
            #    "type": str
            # },
            "vpn_user_connected": {
                "data_path": "data.init.boxConnections",
                "type": dict,
                "next": {
                    "type": str,
                    "value_function": lambda data: data.get("connected"),
                    "tags_function": lambda data: {"name": data.get("name"), "vpn_type": "WireGuard"}
                },
                "exclude_filter_function": lambda data: not isinstance(grab(data, "data.init.boxConnections"), dict)
            },
            "vpn_user_active": {
                "data_path": "data.init.boxConnections",
                "type": dict,
                "next": {
                    "type": str,
                    "value_function": lambda data: data.get("active"),
                    "tags_function": lambda data: {"name": data.get("name"), "vpn_type": "WireGuard"}
                },
                "exclude_filter_function": lambda data: not isinstance(grab(data, "data.init.boxConnections"), dict)
            },
            "vpn_user_virtual_address": {
                "data_path": "data.init.boxConnections",
                "type": dict,
                "next": {
                    "type": str,
                    "value_function": lambda data: data.get("remoteNet"),
                    "tags_function": lambda data: {"name": data.get("name"), "vpn_type": "WireGuard"}
                },
                "exclude_filter_function": lambda data: not isinstance(grab(data, "data.init.boxConnections"), dict)
            },
            "vpn_user_remote_address": {
                "data_path": "data.init.boxConnections",
                "type": dict,
                "next": {
                    "type": str,
                    "value_function": lambda data: data.get("remoteIp"),
                    "tags_function": lambda data: {"name": data.get("name"), "vpn_type": "WireGuard"}
                },
                "exclude_filter_function": lambda data: not isinstance(grab(data, "data.init.boxConnections"), dict)
            },
            "vpn_user_num_active": {
                "type": int,
                "value_function": (lambda data:
                                   len(
                                    [x for x in grab(data, "data.init.boxConnections", fallback=dict()).values()
                                        if x.get("connected") is True]
                                   )
                                   ),
                "tags": {
                    "vpn_type": "WireGuard"
                },
                "exclude_filter_function": lambda data: not isinstance(grab(data, "data.init.boxConnections"), dict)
            }
        }
    }
)
