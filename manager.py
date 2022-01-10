#!/usr/bin/env python
import fire
from managers import openvpn

class Manage(object):

    def __init__(self):
        self.openvpn = openvpn.OpenVpn()

    def vpn_status(self):
        status = self.openvpn.status
        print("VPN IS:",status())

    def vpn_up(self, config_file_path):
        status = self.openvpn.up(config_file_path)
        if status:
            print("VPN IS: UP")
        else:
            print("VPN IS: DOWN")

    def vpn_down(self):
        status = self.openvpn.down
        if status:
            print("VPN IS: DOWN")
        else:
            print("VPN IS: ERROR")

if __name__ == '__main__':
  fire.Fire(Manage)