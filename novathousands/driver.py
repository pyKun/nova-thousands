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
