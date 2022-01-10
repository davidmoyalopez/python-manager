#!/usr/bin/env python
import fire
from managers import openvpn

class Manage(object):

    def __init__(self):
        self.openvpn = openvpn.OpenVpn()

    def vpn_status(self):
        status = self.openvpn.status
        print("VPN IS:",status())

    def vpn_up(self):
        status = self.openvpn.up
        print("VPN IS:",status())

    def vpn_down(self):
        status = self.openvpn.down
        print("VPN IS:",status())

if __name__ == '__main__':
  fire.Fire(Manage)