#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Kun Huang <academicgareth@gmail.com>

import copy
import sys
import ConfigParser

# TODO need cfg.CONF instead
# at least two requeriments:
# 1, keep this CONF alone with children process' CONF
# 2, re-struct config file if necessary, but we must keep it friendly to ops
#    guys

DEFAULT_CONFIG_FILE = '/Users/Gareth/celtics/nova-thousands/etc/nova-thousands.conf'
DEFAULT_TEMPLATE = {'boot_time': '30',
                    'boot_time_deviation': '0'}

def parse_config():
    config = ConfigParser.ConfigParser()
    config.read(DEFAULT_CONFIG_FILE)
    return config


def main():
    config = parse_config()
    default = config.defaults()
    templates = {}
    ports = []

    for sec in config.sections():
        _temp = dict(config.items(sec))
        for key in default:
            del _temp[key]

        if sec.startswith('template:'):
            name = sec[len('template:'):]
            templates[name] = copy.deepcopy(DEFAULT_TEMPLATE)
            templates[name].update(_temp) # TODO Template(_temp)
        elif sec.startswith('port:'):
            _temp['name'] = sec[len('port:'):]
            ports.append(_temp) # TODO Port(_item)

    # TODO fork processes to run nova compute services
    # debug: print config object

    # hang farther process after fork

main()
