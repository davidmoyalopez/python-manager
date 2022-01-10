from subprocess import run, Popen, PIPE
import os
import time


class OpenVpn(object):

    sudo_pass = ''
    file_path = "/tmp/.sudo_pass.txt"

    def __init__(self):
        if os.path.isfile(self.file_path) and self.time_live():
            file = open(self.file_path, "r")
            self.sudo_pass = file.read()
            file.close()
        else:
            password = input("add sudo password:")
            self.sudo_pass = password
            file = open(self.file_path, "w")
            file.write(self.sudo_pass)
            file.close()
    
    def status(self):
        pid = Popen(["pidof", "openvpn"], stdout=PIPE)
        output, error = pid.communicate()
        if output:
            return "UP"
        else:
            return "DOWN"

    def time_live(self):
        now = time.time()
        live = now - 86400
        time_creation_file = os.path.getmtime(self.file_path)
        if time_creation_file > live:
            return True
        else:
            return False
    
    def delete_password(self):
        try:
            os.remove(self.file_path)
        except OSError as e:
            print("Error: %s : %s" % (self.file_path, e.strerror))

    def up(self, config_file_path):
        subprocess = Popen(["sudo", "-S", "openvpn", "--route-gateway", "dhcp", "--allow-pull-fqdn", "--config", config_file_path], stderr=PIPE, stdin=PIPE, universal_newlines=True)
        out, err = subprocess.communicate(self.sudo_pass + '\n')
        if 'incorrect' in err: 
            self.delete_password()
            return "ERROR"
        return True

    def down(self):
        pid = Popen(["pidof", "openvpn"], stdout=PIPE)
        output, error = pid.communicate()
        PID = output.split(None, 1)[0]
        subprocess = Popen(["sudo", "-S", "kill", "-9", PID], stderr=PIPE, stdin=PIPE, universal_newlines=True)
        out, err = subprocess.communicate(self.sudo_pass + '\n')
        if 'incorrect' in err: 
            self.delete_password()
            return "ERROR"
        return True