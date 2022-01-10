from managers import openvpn

def test_status():
    assert openvpn.OpenVpn.status == "DOWN" or "UP"

def test_up():
    assert openvpn.OpenVpn.up == "UP"

def test_down():
    assert openvpn.OpenVpn.down == "DOWN"