#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Kun Huang <academicgareth@gmail.com>

from nova.virt import driver
class NovaThousandsDriver(driver.ComputeDriver):
    '''
    Nova Thousands Compute Driver.
    '''
    def __init__(self, virtapi):
        self.virtapi = virtapi
        self._compute_event_callback = None
        self.instances = []

    def init_host(self, host):
        '''raise error when init failed'''
        return 'Im okay'

    def list_instances(self):
        return self.instances

    def list_instance_uuids(self):
        return [ i['uuid'] for i in self.instances]

    def get_host_stats(self, refresh=False):
        stat = []
        host_stat = {
            'vcpu': 9999,
            'memory_mb': 999999,
            'local_gb': 999999,
            'vcpu_used': 0,
            'memory_mb_used': 0,
            'local_gb_used': 0,
            'hypervisor_type': 'thousands',
            'hypervisor_version': '1.0',
            'hypervisor_hostname': 'thousands001',
            'cpu_info': {},
            'disk_available_least': 9999999,
            }
        stat.append(host_stat)
        return stat
